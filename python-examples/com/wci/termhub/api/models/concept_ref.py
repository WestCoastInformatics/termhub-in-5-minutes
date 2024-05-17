# coding: utf-8

"""
    Terminology Hub Terminology Terminology API

    API documentation for the interacting with terminologies and concepts. <p>For a guided tour of using this API, see our github project <a href=\"https://github.com/terminologyhub/termhub-in-5-minutes\">https://github.com/terminologyhub/termhub-in-5-minutes</a></p>

    The version of the OpenAPI document: 1.0.0
    Contact: info@terminologyhub.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class ConceptRef(BaseModel):
    """
    Represents enough information to uniquely reference a concept in a terminology
    """ # noqa: E501
    id: StrictStr = Field(description="Unique identifier")
    confidence: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Confidence value (for use with search results)")
    modified: Optional[datetime] = Field(default=None, description="Last modified date")
    created: Optional[datetime] = Field(default=None, description="Created date")
    modified_by: Optional[StrictStr] = Field(default=None, description="Last modified by", alias="modifiedBy")
    local: Optional[StrictBool] = Field(default=None, description="Indicates whether this data element is locally created")
    active: Optional[StrictBool] = Field(default=None, description="Indicates whether or not the component is active")
    name: Optional[StrictStr] = None
    code: Optional[StrictStr] = Field(default=None, description="Terminology code, typically representing a unit of meaning")
    terminology: Optional[StrictStr] = Field(default=None, description="Terminology abbreviation, e.g. \"SNOMEDCT\"")
    version: Optional[StrictStr] = Field(default=None, description="Terminology version, e.g. \"20230901\"")
    publisher: Optional[StrictStr] = Field(default=None, description="Terminology publisher, e.g. \"SNOMEDCT\"")
    leaf: Optional[StrictBool] = Field(default=None, description="Indicates whether or not this concept is a leaf node in its hierarchy")
    defined: Optional[StrictBool] = Field(default=None, description="Indicates whether or not this concept has a logical definition with necessary and sufficient conditions")
    __properties: ClassVar[List[str]] = ["id", "confidence", "modified", "created", "modifiedBy", "local", "active", "name", "code", "terminology", "version", "publisher", "leaf", "defined"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ConceptRef from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConceptRef from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "confidence": obj.get("confidence"),
            "modified": obj.get("modified"),
            "created": obj.get("created"),
            "modifiedBy": obj.get("modifiedBy"),
            "local": obj.get("local"),
            "active": obj.get("active"),
            "name": obj.get("name"),
            "code": obj.get("code"),
            "terminology": obj.get("terminology"),
            "version": obj.get("version"),
            "publisher": obj.get("publisher"),
            "leaf": obj.get("leaf"),
            "defined": obj.get("defined")
        })
        return _obj

