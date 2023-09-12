<a name="top"/>

Termhub in 5 Minutes: bash Tutorial
===================================================

This tutorial shows how to use bash scripts to access content from the TermHub Terminology API.

Prerequisites
-------------
* curl must be installed ([Download cURL](https://curl.haxx.se/dlwiz/))
* jq must be installed ([Download jq](https://stedolan.github.io/jq/download/))
* bash must be installed

The various scripts make use of the local `url.env` file to define the API URL.

When using a url.env that points to an instance (such as https://api.terminologyhub.com) that
requires authentication, the login.sh script must first be used to obtain an access
token. All scripts accept a --help flag with additional examples.

Test Scripts
------------
- [login.sh](#login-sh)
- [get-terminologies.sh](#get-terminologies-sh)
- [get-terminology.sh](#get-terminology-sh)
- [get-concept.sh](#get-concept-sh)
- [get-concept-relationships.sh](#get-concept-relationships-sh)
- [get-concept-treepos.sh](#get-concept-treepos-sh)
- [find-concepts.sh](#find-concepts-sh)

The following examples can be typed into the command line of any terminal that has bash, cURL and jq installed.  Run each script with no parameters for examples of how to call each one.

### login.sh

Login to TermHub via username and password.
When finished, copy/past the "token=..." to set a local variable that
can be easily used for further calls.

NOTE: for instances of the server that have login disabled, simply use "guest" as the token.

```
$ ./login.sh username "password"
-----------------------------------------------------
Starting ...Mon, Sep 11, 2023  7:14:20 PM
-----------------------------------------------------
url = https://api.terminologyhub.com
username = bacarlsen@example.com
password = ************

  token=eyJ0eXAi...9U0lwZknkQrug

-----------------------------------------------------
Finished ...Mon, Sep 11, 2023  7:14:21 PM
-----------------------------------------------------
```

From the output, paste the "token=..." into your shell to set it as a variable for the following calls.

[Back to Top](#top)

<a name="get-terminologies-sh"/>

### get-terminologies.sh

Return all loaded terminologies currently hosted by the API.

```
$ ./get-terminologies.sh --token $token
-----------------------------------------------------
Starting ...Mon, Sep 11, 2023  7:15:45 PM
-----------------------------------------------------
url = https://api.terminologyhub.com

  Performing terminologies lookup
    count = 3

    {
      "total": 33,
      "parameters": {
        "query": "loaded:true",
        "limit": 10,
        "offset": 0
      },
      "items": [
        {
          "id": "7778a80f-8c2b-439b-86fd-955bb6c01d0e",
          "confidence": 0.012578782625496387,
          "modified": "2023-09-03T01:00:49.665+00:00",
          "created": "2023-09-03T01:00:49.665+00:00",
          "modifiedBy": "loader",
          "local": false,
          "active": true,
          "abbreviation": "SNOMEDCT",
          "name": "Systematized Nomenclature of Medicine–Clinical Terminology",
          "version": "20230131",
          "publisher": "NLM",
          "latest": false,
          "loaded": true,
          "family": "SNOMEDCT",
          "releaseDate": "2023-01-31",
          "license": "UNRESTRICTED",
          "attributes": {
            "tree-positions": "true"
          },
          "conceptCt": 500356,
          "relationshipCt": 1219695,
          "treePositionCt": 13270514
        },
        ...
        {
          "id": "001c37aa-d414-492a-9278-5bb8163c806e",
          "confidence": 0.012578782625496387,
          "modified": "2023-09-06T01:20:28.876+00:00",
          "created": "2023-09-06T01:20:28.876+00:00",
          "modifiedBy": "loader",
          "local": false,
          "active": true,
          "abbreviation": "SNOMEDCT_US",
          "name": "Systematized Nomenclature of Medicine–Clinical Terminology, US Edition",
          "version": "20230301",
          "publisher": "SANDBOX",
          "latest": true,
          "loaded": true,
          "family": "SNOMEDCT",
          "releaseDate": "2023-03-01",
          "license": "UNRESTRICTED",
          "attributes": {
            "tree-positions": "true"
          },
          "conceptCt": 416,
          "relationshipCt": 676,
          "treePositionCt": 2011
        }
      ]
    }

-----------------------------------------------------
Finished ...Mon, Sep 11, 2023  7:15:45 PM
-----------------------------------------------------
```

[Back to Top](#top)

<a name="get-terminology-sh"/>

### get-terminologies.sh

Return the specific terminology for the abbreviation, publisher, and version.

```
$ ./get-terminology.sh --token $token SNOMEDCT SANDBOX 20230731
TBD
```

```
$ ./get-terminology.sh --token $token ICD10CM SANDBOX 2023

```

[Back to Top](#top)

<a name="get-concept-sh"/>

### get-concept.sh

Return summary concept information for a given terminology and code.  The following
example gets the 73211009 | Diabetes mellitus | concept in SNOMEDCT.

```
$ ./get-concept.sh SNOMEDCT SANDBOX 20230731 73211009 --token $token
-----------------------------------------------------
Starting ...Mon, Sep 11, 2023  7:41:19 PM
-----------------------------------------------------
url = https://api.terminologyhub.com
terminology = SNOMEDCT
publisher = SANDBOX
version = 20230731
code = 73211009

  Get concept for SNOMEDCT 73211009:

    {
      "id": "32820a45-c767-45ac-bac0-3655410af1f7",
      "confidence": 23.66806411743164,
      "modified": "2002-01-31T00:00:00.000+00:00",
      "created": "2002-01-31T00:00:00.000+00:00",
      "modifiedBy": "loader",
      "local": false,
      "active": true,
      "name": "Diabetes mellitus",
      "code": "73211009",
      "terminology": "SNOMEDCT",
      "version": "20230731",
      "publisher": "SANDBOX",
      "leaf": true,
      "defined": false,
      "normName": "diabetes mellitus",
      "stemName": "diabet mellitus",
      "terms": [
        {
          "id": "8b5bec36-cfcd-418b-a19a-ab444ecdc208",
          "modified": "2002-01-31T00:00:00.000+00:00",
          "created": "2002-01-31T00:00:00.000+00:00",
          "modifiedBy": "loader",
          "local": false,
          "active": false,
          "name": "Diabetes mellitus, NOS",
          "normName": "diabetes mellitus nos",
          "stemName": "diabet mellitus nos",
          "wordCt": 3,
          "terminology": "SNOMEDCT",
          "version": "20230731",
          "publisher": "SANDBOX",
          "componentId": "121590018",
          "code": "73211009",
          "conceptId": "73211009",
          "localeMap": {
            "en": false
          },
          "type": "900000000000013009",
          "attributes": {
            "caseSignificanceId": "900000000000020002",
            "moduleId": "900000000000207008"
          }
        },
        {
          "id": "0d0d12fc-8940-4271-b7dd-ef6027773cd1",
          "modified": "2017-07-31T00:00:00.000+00:00",
          "created": "2017-07-31T00:00:00.000+00:00",
          "modifiedBy": "loader",
          "local": false,
          "active": true,
          "name": "Diabetes mellitus",
          "normName": "diabetes mellitus",
          "stemName": "diabet mellitus",
          "wordCt": 2,
          "terminology": "SNOMEDCT",
          "version": "20230731",
          "publisher": "SANDBOX",
          "componentId": "121589010",
          "code": "73211009",
          "conceptId": "73211009",
          "localeMap": {
            "en_GB": true,
            "en": true
          },
          "type": "900000000000013009",
          "attributes": {
            "caseSignificanceId": "900000000000448009",
            "moduleId": "900000000000207008"
          }
        },
        {
          "id": "ae7c5155-19b9-4a0e-80c2-31f8523efb80",
          "modified": "2017-07-31T00:00:00.000+00:00",
          "created": "2017-07-31T00:00:00.000+00:00",
          "modifiedBy": "loader",
          "local": false,
          "active": true,
          "name": "Diabetes mellitus (disorder)",
          "normName": "diabetes mellitus disorder",
          "stemName": "diabet mellitus disord",
          "wordCt": 3,
          "terminology": "SNOMEDCT",
          "version": "20230731",
          "publisher": "SANDBOX",
          "componentId": "813575016",
          "code": "73211009",
          "conceptId": "73211009",
          "localeMap": {
            "en_GB": true,
            "en": true
          },
          "type": "900000000000003001",
          "attributes": {
            "caseSignificanceId": "900000000000448009",
            "moduleId": "900000000000207008"
          }
        },
        {
          "id": "1e371c1f-5089-4cd7-9bb1-7ce1fc618dae",
          "modified": "2002-01-31T00:00:00.000+00:00",
          "created": "2002-01-31T00:00:00.000+00:00",
          "modifiedBy": "loader",
          "local": false,
          "active": true,
          "name": "DM - Diabetes mellitus",
          "normName": "dm diabetes mellitus",
          "stemName": "dm diabet mellitus",
          "wordCt": 3,
          "terminology": "SNOMEDCT",
          "version": "20230731",
          "publisher": "SANDBOX",
          "componentId": "502372015",
          "code": "73211009",
          "conceptId": "73211009",
          "localeMap": {
            "en_GB": false,
            "en": false
          },
          "type": "900000000000013009",
          "attributes": {
            "caseSignificanceId": "900000000000017005",
            "moduleId": "900000000000207008"
          }
        }
      ],
      "attributes": {
        "definitionStatusId": "900000000000074008",
        "moduleId": "900000000000207008"
      },
      "semanticTypes": [
        "disorder"
      ]
    }

-----------------------------------------------------
Finished ...Mon, Sep 11, 2023  7:41:19 PM
-----------------------------------------------------
```

[Back to Top](#top)

<a name="get-concept-relationships-sh"/>

### get-concept-relationships.sh

Return concept relationship information for a given terminology and code. The 
following example finds relationships for the 73211009 | Diabetes mellitus | concept in 
SNOMEDCT_US.  It limits the results to 5 entries and sorts by the "additionalType"
field.

```
$ ./get-concept-relationships.sh SNOMEDCT SANDBOX 20230731 73211009 --token $token
-----------------------------------------------------
Starting ...Mon, Sep 11, 2023  7:44:30 PM
-----------------------------------------------------
url = https://api.terminologyhub.com
terminology = SNOMEDCT
code = 73211009

  Get concept for SNOMEDCT 73211009:

    {
      "total": 3,
      "parameters": {
        "query": "terminology:SNOMEDCT AND publisher:SANDBOX AND version:20230731 AND from.code:73211009",
        "limit": 10,
        "offset": 0
      },
      "items": [
        {
          "id": "b576d52c-2b88-4093-83d0-c663f5c8a842",
          "confidence": 25.006900787353516,
          "modified": "2012-01-31T00:00:00.000+00:00",
          "created": "2012-01-31T00:00:00.000+00:00",
          "modifiedBy": "loader",
          "local": false,
          "active": true,
          "terminology": "SNOMEDCT",
          "version": "20230731",
          "publisher": "SANDBOX",
          "componentId": "4601709020",
          "type": "Is a",
          "additionalType": "116680003",
          "from": {
            "id": "32820a45-c767-45ac-bac0-3655410af1f7",
            "modified": "2002-01-31T00:00:00.000+00:00",
            "created": "2002-01-31T00:00:00.000+00:00",
            "modifiedBy": "loader",
            "local": false,
            "active": true,
            "name": "Diabetes mellitus",
            "code": "73211009",
            "terminology": "SNOMEDCT",
            "version": "20230731",
            "publisher": "SANDBOX",
            "leaf": false
          },
          "to": {
            "id": "214cecaa-7860-4945-b649-50cba67590a6",
            "modified": "2002-01-31T00:00:00.000+00:00",
            "created": "2002-01-31T00:00:00.000+00:00",
            "modifiedBy": "loader",
            "local": false,
            "active": true,
            "name": "Disorder of endocrine system",
            "code": "362969004",
            "terminology": "SNOMEDCT",
            "version": "20230731",
            "publisher": "SANDBOX",
            "leaf": false
          },
          "hierarchical": true,
          "asserted": true,
          "defining": true,
          "group": "0"
        },
        {
          "id": "43d5b738-a48f-4f00-a3c7-96e7a14db22f",
          "confidence": 25.006900787353516,
          "modified": "2019-07-31T00:00:00.000+00:00",
          "created": "2019-07-31T00:00:00.000+00:00",
          "modifiedBy": "loader",
          "local": false,
          "active": true,
          "terminology": "SNOMEDCT",
          "version": "20230731",
          "publisher": "SANDBOX",
          "componentId": "4601710026",
          "type": "other",
          "additionalType": "363698007",
          "from": {
            "id": "32820a45-c767-45ac-bac0-3655410af1f7",
            "modified": "2002-01-31T00:00:00.000+00:00",
            "created": "2002-01-31T00:00:00.000+00:00",
            "modifiedBy": "loader",
            "local": false,
            "active": true,
            "name": "Diabetes mellitus",
            "code": "73211009",
            "terminology": "SNOMEDCT",
            "version": "20230731",
            "publisher": "SANDBOX",
            "leaf": false
          },
          "to": {
            "id": "a94fa73a-ad28-4221-a976-00268df5ff9f",
            "modified": "2002-01-31T00:00:00.000+00:00",
            "created": "2002-01-31T00:00:00.000+00:00",
            "modifiedBy": "loader",
            "local": false,
            "active": true,
            "name": "Structure of endocrine system",
            "code": "113331007",
            "terminology": "SNOMEDCT",
            "version": "20230731",
            "publisher": "SANDBOX",
            "leaf": false
          },
          "hierarchical": false,
          "asserted": true,
          "defining": true,
          "group": "1"
        },
        {
          "id": "09761540-b50f-4a1d-afcf-9575f5d2a3a4",
          "confidence": 25.006900787353516,
          "modified": "2002-01-31T00:00:00.000+00:00",
          "created": "2002-01-31T00:00:00.000+00:00",
          "modifiedBy": "loader",
          "local": false,
          "active": true,
          "terminology": "SNOMEDCT",
          "version": "20230731",
          "publisher": "SANDBOX",
          "componentId": "267149027",
          "type": "Is a",
          "additionalType": "116680003",
          "from": {
            "id": "32820a45-c767-45ac-bac0-3655410af1f7",
            "modified": "2002-01-31T00:00:00.000+00:00",
            "created": "2002-01-31T00:00:00.000+00:00",
            "modifiedBy": "loader",
            "local": false,
            "active": true,
            "name": "Diabetes mellitus",
            "code": "73211009",
            "terminology": "SNOMEDCT",
            "version": "20230731",
            "publisher": "SANDBOX",
            "leaf": false
          },
          "to": {
            "id": "23c24f49-5d2e-44fd-9bed-194b95936054",
            "modified": "2002-01-31T00:00:00.000+00:00",
            "created": "2002-01-31T00:00:00.000+00:00",
            "modifiedBy": "loader",
            "local": false,
            "active": true,
            "name": "Disorder of glucose metabolism",
            "code": "126877002",
            "terminology": "SNOMEDCT",
            "version": "20230731",
            "publisher": "SANDBOX",
            "leaf": false
          },
          "hierarchical": true,
          "asserted": true,
          "defining": true,
          "group": "0"
        }
      ]
    }

-----------------------------------------------------
Finished ...Mon, Sep 11, 2023  7:44:30 PM
-----------------------------------------------------
```

[Back to Top](#top)

<a name="get-concept-treepos-sh"/>

### get-concept-treepos.sh

Return concept relationship information for a given terminology and code. The 
following example finds relationships for the 73211009 | Diabetes mellitus | concept in 
SNOMEDCT.  It limits the results to 5 entries and sorts by the "additionalType"
field.

```
$ ./get-concept-treepos.sh SNOMEDCT SANDBOX 20230731 73211009 --token $token
-----------------------------------------------------
Starting ...Mon, Sep 11, 2023  7:46:57 PM
-----------------------------------------------------
url = https://api.terminologyhub.com
terminology = SNOMEDCT
code = 73211009

  Get concept for SNOMEDCT 73211009:

    {
      "total": 2,
      "parameters": {
        "query": "terminology:SNOMEDCT AND publisher:SANDBOX AND version:20230731 AND concept.code:73211009",
        "limit": 10,
        "offset": 0
      },
      "items": [
        {
          "id": "c4deea09-6059-43bd-a248-6a3fd92bf05f",
          "confidence": 41.982330322265625,
          "modified": "2023-09-06T01:25:50.416+00:00",
          "created": "2023-09-06T01:25:50.416+00:00",
          "modifiedBy": "loader",
          "local": false,
          "active": true,
          "terminology": "SNOMEDCT",
          "version": "20230731",
          "publisher": "SANDBOX",
          "concept": {
            "id": "7ae1a8d1-742d-43c7-9de6-2b6712bb2aa4",
            "local": false,
            "active": true,
            "name": "SNOMED CT Concept",
            "code": "138875005",
            "leaf": false
          },
          "additionalType": "116680003",
          "childCt": 7,
          "children": [
            {
              "id": "d045d5c1-c68c-48bb-a6cf-2b045f16d38e",
              "confidence": 40.35016632080078,
              "modified": "2023-09-06T01:25:50.500+00:00",
              "created": "2023-09-06T01:25:50.500+00:00",
              "modifiedBy": "loader",
              "local": false,
              "active": true,
              "terminology": "SNOMEDCT",
              "version": "20230731",
              "publisher": "SANDBOX",
              "concept": {
                "id": "ae540c62-1aab-42d5-b0d5-5ca0662c4436",
                "local": false,
                "active": true,
                "name": "Clinical finding",
                "code": "404684003",
                "leaf": false
              },
              "additionalType": "116680003",
              "ancestorPath": "138875005",
              "childCt": 4,
              "children": [
                {
                  "id": "19ad0f82-20b5-4fa1-9042-296c8377f7d4",
                  "confidence": 38.87129211425781,
                  "modified": "2023-09-06T01:25:50.502+00:00",
                  "created": "2023-09-06T01:25:50.502+00:00",
                  "modifiedBy": "loader",
                  "local": false,
                  "active": true,
                  "terminology": "SNOMEDCT",
                  "version": "20230731",
                  "publisher": "SANDBOX",
                  "concept": {
                    "id": "db882dc6-f508-415e-8945-3ffdd1521208",
                    "local": false,
                    "active": true,
                    "name": "Disease",
                    "code": "64572001",
                    "leaf": false
                  },
                  "additionalType": "116680003",
                  "ancestorPath": "138875005~404684003",
                  "childCt": 5,
                  "children": [
                    {
                      "id": "8902482a-2f68-4da6-92f6-05ba9b1f43ea",
                      "confidence": 38.61029052734375,
                      "modified": "2023-09-06T01:25:50.502+00:00",
                      "created": "2023-09-06T01:25:50.502+00:00",
                      "modifiedBy": "loader",
                      "local": false,
                      "active": true,
                      "terminology": "SNOMEDCT",
                      "version": "20230731",
                      "publisher": "SANDBOX",
                      "concept": {
                        "id": "4b3558d9-7c32-4669-8de1-074faf4b3cbf",
                        "local": false,
                        "active": true,
                        "name": "Disorder of body system",
                        "code": "362965005",
                        "leaf": false
                      },
                      "additionalType": "116680003",
                      "ancestorPath": "138875005~404684003~64572001",
                      "childCt": 3,
                      "children": [
                        {
                          "id": "c3343616-8d17-4ca1-bbfe-3735c28af048",
                          "confidence": 39.647464752197266,
                          "modified": "2023-09-06T01:25:50.502+00:00",
                          "created": "2023-09-06T01:25:50.502+00:00",
                          "modifiedBy": "loader",
                          "local": false,
                          "active": true,
                          "terminology": "SNOMEDCT",
                          "version": "20230731",
                          "publisher": "SANDBOX",
                          "concept": {
                            "id": "214cecaa-7860-4945-b649-50cba67590a6",
                            "local": false,
                            "active": true,
                            "name": "Disorder of endocrine system",
                            "code": "362969004",
                            "leaf": false
                          },
                          "additionalType": "116680003",
                          "ancestorPath": "138875005~404684003~64572001~362965005",
                          "childCt": 1,
                          "children": [
                            {
                              "id": "ebb6d961-6771-4cc8-861d-027398f07732",
                              "confidence": 39.02238845825195,
                              "modified": "2023-09-06T01:25:50.502+00:00",
                              "created": "2023-09-06T01:25:50.502+00:00",
                              "modifiedBy": "loader",
                              "local": false,
                              "active": true,
                              "terminology": "SNOMEDCT",
                              "version": "20230731",
                              "publisher": "SANDBOX",
                              "concept": {
                                "id": "32820a45-c767-45ac-bac0-3655410af1f7",
                                "local": false,
                                "active": true,
                                "name": "Diabetes mellitus",
                                "code": "73211009",
                                "leaf": true
                              },
                              "additionalType": "116680003",
                              "ancestorPath": "138875005~404684003~64572001~362965005~362969004",
                              "childCt": 0
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "id": "c4deea09-6059-43bd-a248-6a3fd92bf05f",
          "confidence": 41.982330322265625,
          "modified": "2023-09-06T01:25:50.416+00:00",
          "created": "2023-09-06T01:25:50.416+00:00",
          "modifiedBy": "loader",
          "local": false,
          "active": true,
          "terminology": "SNOMEDCT",
          "version": "20230731",
          "publisher": "SANDBOX",
          "concept": {
            "id": "7ae1a8d1-742d-43c7-9de6-2b6712bb2aa4",
            "local": false,
            "active": true,
            "name": "SNOMED CT Concept",
            "code": "138875005",
            "leaf": false
          },
          "additionalType": "116680003",
          "childCt": 7,
          "children": [
            {
              "id": "d045d5c1-c68c-48bb-a6cf-2b045f16d38e",
              "confidence": 40.35016632080078,
              "modified": "2023-09-06T01:25:50.500+00:00",
              "created": "2023-09-06T01:25:50.500+00:00",
              "modifiedBy": "loader",
              "local": false,
              "active": true,
              "terminology": "SNOMEDCT",
              "version": "20230731",
              "publisher": "SANDBOX",
              "concept": {
                "id": "ae540c62-1aab-42d5-b0d5-5ca0662c4436",
                "local": false,
                "active": true,
                "name": "Clinical finding",
                "code": "404684003",
                "leaf": false
              },
              "additionalType": "116680003",
              "ancestorPath": "138875005",
              "childCt": 4,
              "children": [
                {
                  "id": "19ad0f82-20b5-4fa1-9042-296c8377f7d4",
                  "confidence": 38.87129211425781,
                  "modified": "2023-09-06T01:25:50.502+00:00",
                  "created": "2023-09-06T01:25:50.502+00:00",
                  "modifiedBy": "loader",
                  "local": false,
                  "active": true,
                  "terminology": "SNOMEDCT",
                  "version": "20230731",
                  "publisher": "SANDBOX",
                  "concept": {
                    "id": "db882dc6-f508-415e-8945-3ffdd1521208",
                    "local": false,
                    "active": true,
                    "name": "Disease",
                    "code": "64572001",
                    "leaf": false
                  },
                  "additionalType": "116680003",
                  "ancestorPath": "138875005~404684003",
                  "childCt": 5,
                  "children": [
                    {
                      "id": "db68a22a-410b-4edd-a50c-0721c0fe8079",
                      "confidence": 38.669132232666016,
                      "modified": "2023-09-06T01:25:50.502+00:00",
                      "created": "2023-09-06T01:25:50.502+00:00",
                      "modifiedBy": "loader",
                      "local": false,
                      "active": true,
                      "terminology": "SNOMEDCT",
                      "version": "20230731",
                      "publisher": "SANDBOX",
                      "concept": {
                        "id": "4ed9893c-82ff-4e94-8d07-092010f6eb3e",
                        "local": false,
                        "active": true,
                        "name": "Metabolic disease",
                        "code": "75934005",
                        "leaf": false
                      },
                      "additionalType": "116680003",
                      "ancestorPath": "138875005~404684003~64572001",
                      "childCt": 1,
                      "children": [
                        {
                          "id": "ac80c910-2d94-4b09-835a-eb3ca508f8f4",
                          "confidence": 39.84139633178711,
                          "modified": "2023-09-06T01:25:50.502+00:00",
                          "created": "2023-09-06T01:25:50.502+00:00",
                          "modifiedBy": "loader",
                          "local": false,
                          "active": true,
                          "terminology": "SNOMEDCT",
                          "version": "20230731",
                          "publisher": "SANDBOX",
                          "concept": {
                            "id": "a97b4841-5a9a-46a0-b380-f9cd0b848a0c",
                            "local": false,
                            "active": true,
                            "name": "Disorder of carbohydrate metabolism",
                            "code": "20957000",
                            "leaf": false
                          },
                          "additionalType": "116680003",
                          "ancestorPath": "138875005~404684003~64572001~75934005",
                          "childCt": 1,
                          "children": [
                            {
                              "id": "58b23376-d6c8-49c6-aed2-24ee0248f29e",
                              "confidence": 40.62815475463867,
                              "modified": "2023-09-06T01:25:50.502+00:00",
                              "created": "2023-09-06T01:25:50.502+00:00",
                              "modifiedBy": "loader",
                              "local": false,
                              "active": true,
                              "terminology": "SNOMEDCT",
                              "version": "20230731",
                              "publisher": "SANDBOX",
                              "concept": {
                                "id": "23c24f49-5d2e-44fd-9bed-194b95936054",
                                "local": false,
                                "active": true,
                                "name": "Disorder of glucose metabolism",
                                "code": "126877002",
                                "leaf": false
                              },
                              "additionalType": "116680003",
                              "ancestorPath": "138875005~404684003~64572001~75934005~20957000",
                              "childCt": 1,
                              "children": [
                                {
                                  "id": "698c92a4-67ba-434b-b7c3-6859eadb6dd3",
                                  "confidence": 41.59420394897461,
                                  "modified": "2023-09-06T01:25:50.502+00:00",
                                  "created": "2023-09-06T01:25:50.502+00:00",
                                  "modifiedBy": "loader",
                                  "local": false,
                                  "active": true,
                                  "terminology": "SNOMEDCT",
                                  "version": "20230731",
                                  "publisher": "SANDBOX",
                                  "concept": {
                                    "id": "32820a45-c767-45ac-bac0-3655410af1f7",
                                    "local": false,
                                    "active": true,
                                    "name": "Diabetes mellitus",
                                    "code": "73211009",
                                    "leaf": true
                                  },
                                  "additionalType": "116680003",
                                  "ancestorPath": "138875005~404684003~64572001~75934005~20957000~126877002",
                                  "childCt": 0
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }

-----------------------------------------------------
Finished ...Mon, Sep 11, 2023  7:46:58 PM
-----------------------------------------------------
```

[Back to Top](#top)

<a name="find-concepts-sh"/>

### find-concepts.sh

Used to perform text searches to find matching concepts. The following example
performs a text search for "diabetes mellitus" and limits search results to 5
entries.

```
$ ./find-concepts.sh SNOMEDCT SANDBOX 20230731 "diabetes mellitus" --token $token --limit 5
-----------------------------------------------------
Starting ...Mon, Sep 11, 2023  7:49:01 PM
-----------------------------------------------------
url = https://api.terminologyhub.com
terminology = SNOMEDCT
publisher = SANDBOX
version = 20230731
query = diabetes mellitus
expr =
offset = 0
limit = 5
sort =
ascending =

  Find concepts: (terminology:SNOMEDCT AND publisher:SANDBOX AND version:20230731) AND diabetes mellitus

    {
      "total": 1,
      "parameters": {
        "query": "(terminology:SNOMEDCT AND publisher:SANDBOX AND version:20230731) AND diabetes mellitus AND ((terminology:ICD10CM AND publisher:SANDBOX AND version:2023) OR (terminology:SNOMEDCT AND publisher:SANDBOX AND version:20230731) OR (terminology:LNC AND publisher:SANDBOX AND version:274) OR (terminology:RXNORM AND publisher:SANDBOX AND version:07032023))",
        "limit": 5,
        "offset": 0
      },
      "items": [
        {
          "id": "32820a45-c767-45ac-bac0-3655410af1f7",
          "confidence": 44.66986846923828,
          "modified": "2002-01-31T00:00:00.000+00:00",
          "created": "2002-01-31T00:00:00.000+00:00",
          "modifiedBy": "loader",
          "local": false,
          "active": true,
          "name": "Diabetes mellitus",
          "code": "73211009",
          "terminology": "SNOMEDCT",
          "version": "20230731",
          "publisher": "SANDBOX",
          "leaf": true,
          "defined": false
        }
      ]
    }

-----------------------------------------------------
Finished ...Mon, Sep 11, 2023  7:49:02 PM
-----------------------------------------------------
```

NEEDS WORK BELOW:
This example performs a search that returns all concept members of the SNOMEDCT_US
reference set 723264001 | Lateralizable body structure reference set |.  When not 
specified the "MIN" resolver is used, which returns only first-class attributes of 
the concept object.  Use "--resolver DEFAULT" for summary concept information about 
each result.

```
$ ./find-concepts.sh SNOMEDCT_US NLM 20210901 "" --expr ^723264001 --limit 5 --token $token
-----------------------------------------------------
Starting ...Thu, Apr  2, 2020  6:34:28 PM
-----------------------------------------------------
url = https://api.terminologyhub.com
terminology = SNOMEDCT_US
query =
resolver = MIN
expr = ^723264001
offset = 0
limit = 5
sort =
ascending =

  Find concepts:

    {
      "total": 19778,
      "limit": 5,
      "offset": 0,
      "items": [
        {
          "id": "e9694627-b34f-488f-b134-7a8e0e13b1ba",
          "local": false,
          "active": true,
          "name": "Pulmonary vein confluence",
          "code": "373097002",
          "terminology": "SNOMEDCT_US"
        },
        {
          "id": "1ed65df3-f320-47e2-bd25-b902678b3658",
          "local": false,
          "active": true,
          "name": "Deiter's cell",
          "code": "4799000",
          "terminology": "SNOMEDCT_US"
        },
        {
          "id": "7358bcab-4791-4378-a094-da9cc83da6e1",
          "local": false,
          "active": true,
          "name": "Cephalometric molar superius point",
          "code": "713770007",
          "terminology": "SNOMEDCT_US"
        },
        {
          "id": "eabb911c-78e5-4a17-b175-459bce6e76fd",
          "local": false,
          "active": true,
          "name": "Cephalometric long axis of lower incisor",
          "code": "713772004",
          "terminology": "SNOMEDCT_US"
        },
        {
          "id": "7099f23d-9304-4f9d-9fda-6d3b579f7b28",
          "local": false,
          "active": true,
          "name": "Tibia and fibula, CS",
          "code": "110536004",
          "terminology": "SNOMEDCT_US"
        }
      ]
    }

-----------------------------------------------------
Finished ...Thu, Apr  2, 2020  6:34:28 PM
-----------------------------------------------------
```

[Back to Top](#top)

<a name="get-subtree-sh"/>

### get-subtree.sh

Used to lookup a subtree for a terminology code.  The following example finds
all of the descendants to a depth of 3 (which for ICD10CM is all of the 
descendants).

```
-----------------------------------------------------
Starting ...Mon, Mar 23, 2020  4:40:37 PM
-----------------------------------------------------
url = https://api.terminologyhub.com
terminology = ICD10CM
code = M01
level = 3

  Get concept for ICD10CM M01:

    {
      "local": false,
      "active": true,
      "terminology": "ICD10CM",
      "code": "M01",
      "name": "Direct infections of joint in infectious and parasitic diseases classified elsewhere",
      "childCt": 1,
      "level": 0,
      "children": [
        {
          "local": false,
          "active": true,
          "terminology": "ICD10CM",
          "code": "M01.X",
          "name": "Direct infection of joint in infectious and parasitic diseases classified elsewhere",
          "childCt": 10,
          "level": 1,
          "children": [
            {
              "local": false,
              "active": true,
              "terminology": "ICD10CM",
              "code": "M01.X0",
              "name": "Direct infection of unspecified joint in infectious and parasitic diseases classified elsewhere",
              "childCt": 0,
              "level": 2
            },
            ...
          ]
        }
      ]
    }

-----------------------------------------------------
Finished ...Mon, Mar 23, 2020  4:40:38 PM
-----------------------------------------------------
```

[Back to Top](#top)

