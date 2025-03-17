# coding: utf-8

"""
    Kubeflow Trainer OpenAPI Spec

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: unversioned
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kubeflow.trainer.models.io_k8s_apimachinery_pkg_apis_meta_v1_preconditions import IoK8sApimachineryPkgApisMetaV1Preconditions
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApimachineryPkgApisMetaV1DeleteOptions(BaseModel):
    """
    DeleteOptions may be provided when deleting an API object.
    """ # noqa: E501
    api_version: Optional[StrictStr] = Field(default=None, description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources", alias="apiVersion")
    dry_run: Optional[List[StrictStr]] = Field(default=None, description="When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed", alias="dryRun")
    grace_period_seconds: Optional[StrictInt] = Field(default=None, description="The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.", alias="gracePeriodSeconds")
    ignore_store_read_error_with_cluster_breaking_potential: Optional[StrictBool] = Field(default=None, description="if set to true, it will trigger an unsafe deletion of the resource in case the normal deletion flow fails with a corrupt object error. A resource is considered corrupt if it can not be retrieved from the underlying storage successfully because of a) its data can not be transformed e.g. decryption failure, or b) it fails to decode into an object. NOTE: unsafe deletion ignores finalizer constraints, skips precondition checks, and removes the object from the storage. WARNING: This may potentially break the cluster if the workload associated with the resource being unsafe-deleted relies on normal deletion flow. Use only if you REALLY know what you are doing. The default value is false, and the user must opt in to enable it", alias="ignoreStoreReadErrorWithClusterBreakingPotential")
    kind: Optional[StrictStr] = Field(default=None, description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds")
    orphan_dependents: Optional[StrictBool] = Field(default=None, description="Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both.", alias="orphanDependents")
    preconditions: Optional[IoK8sApimachineryPkgApisMetaV1Preconditions] = Field(default=None, description="Must be fulfilled before a deletion is carried out. If not possible, a 409 Conflict status will be returned.")
    propagation_policy: Optional[StrictStr] = Field(default=None, description="Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground.", alias="propagationPolicy")
    __properties: ClassVar[List[str]] = ["apiVersion", "dryRun", "gracePeriodSeconds", "ignoreStoreReadErrorWithClusterBreakingPotential", "kind", "orphanDependents", "preconditions", "propagationPolicy"]

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
        """Create an instance of IoK8sApimachineryPkgApisMetaV1DeleteOptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of preconditions
        if self.preconditions:
            _dict['preconditions'] = self.preconditions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoK8sApimachineryPkgApisMetaV1DeleteOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "apiVersion": obj.get("apiVersion"),
            "dryRun": obj.get("dryRun"),
            "gracePeriodSeconds": obj.get("gracePeriodSeconds"),
            "ignoreStoreReadErrorWithClusterBreakingPotential": obj.get("ignoreStoreReadErrorWithClusterBreakingPotential"),
            "kind": obj.get("kind"),
            "orphanDependents": obj.get("orphanDependents"),
            "preconditions": IoK8sApimachineryPkgApisMetaV1Preconditions.from_dict(obj["preconditions"]) if obj.get("preconditions") is not None else None,
            "propagationPolicy": obj.get("propagationPolicy")
        })
        return _obj


