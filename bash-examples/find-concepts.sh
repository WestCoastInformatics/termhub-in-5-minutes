#!/bin/bash
#
# Script to call TermHub to perform term searches to find concept codes.
#
while [[ "$#" -gt 0 ]]; do case $1 in
  --token) token="$2"; shift;;
  --expr) expr="$2"; shift;;
  --offset) offset="$2"; shift;;
  --limit) limit="$2"; shift;;
  --ascending) ascending="$2"; shift;;
  --sort) sort="$2"; shift;;
  *) arr=( "${arr[@]}" "$1" );;
esac; shift; done

if [ ${#arr[@]} -ne 4 ]; then
  echo "Usage: $0 <terminology> <publisher> <version> <query> [--token token] [--expr <expression>]"
  echo "    [--ascending <true|false>] [--sort <sort>]"
  echo "  e.g. $0 SNOMEDCT_US NLM 20210901 '"'"'"malignant melanoma"'"'"' --token \$token"
  echo "  e.g. $0 SNOMEDCT_US NLM 20210901 '"'"'"malignant melanoma"'"'"' --token \$token --limit 5"
  echo "  e.g. $0 SNOMEDCT_US NLM 20210901 '"'"'"malignant melanoma"'"'"' --token \$token"
  echo "  e.g. $0 SNOMEDCT_US NLM 20210901 '"'"'"malignant melanoma"'"'"' --expr disorder --token \$token"
  echo "  e.g. $0 SNOMEDCT_US NLM 20210901 '"'"'"malignant melanoma"'"'"' --expr \"<<363346000 | Malignant neoplastic disease | \" --token \$token"
  echo "  e.g. $0 SNOMEDCT_US NLM 20210901 \"\" --expr \"^723264001 | Lateralizable body structure reference set |\" --token \$token"
  exit 1
fi

terminology=${arr[0]}
publisher=${arr[1]}
version=${arr[2]}
query=${arr[3]}

# import URL into environment from config
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
. $DIR/url.env

echo "-----------------------------------------------------"
echo "Starting ...$(/bin/date)"
echo "-----------------------------------------------------"
echo "url = $url"
echo "terminology = $terminology"
echo "publisher = $publisher"
echo "version = $version"

# Default resolver
if [[ -z $expr ]]; then
  expr=
fi
if [[ -z $offset ]]; then
  offset=0
fi
if [[ -z $limit ]]; then
  limit=10
fi
if [[ -z $ascending ]]; then
  ascending=
fi
if [[ -z $sort ]]; then
  sort=
fi
echo "query = $query"
echo "expr = $expr"
echo "offset = $offset"
echo "limit = $limit"
echo "sort = $sort"
echo "ascending = $ascending"
echo ""

if [[ -z $query ]]; then
    query="(terminology:$terminology AND version:$version)"
else
    query="(terminology:$terminology AND version:$version) AND $query"
fi

# GET call
echo "  Find concepts: $query"
# TODO: --data-urlencode "sort=$sort" 
curl -v -w "\n%{http_code}" -G "$url/terminology/sandbox/concept" -H "Authorization: Bearer $token" --data-urlencode "query=$query" --data-urlencode "limit=$limit" --data-urlencode "offset=$offset" --data-urlencode "ascending=$ascending" --data-urlencode "expression=$expr" --data-urlencode "type=$type" 2> /dev/null > /tmp/x.$$
if [ $? -ne 0 ]; then
  echo "ERROR: GET call failed"
  exit 1
fi

# check status
status=`tail -1 /tmp/x.$$`
if [ $status -ne 200 ]; then
  cat /tmp/x.$$ | sed 's/^/    /'
  echo "ERROR: GET call returned $status, expected 200"
  exit 1
fi

# write output
echo ""
perl -pe 's/200$//' /tmp/x.$$ | jq '.' | sed 's/^/    /'
echo ""

# ---------------------------------------------------------
# Cleanup
#
/bin/rm -f /tmp/x.$$

echo "-----------------------------------------------------"
echo "Finished ...`/bin/date`"
echo "-----------------------------------------------------"
