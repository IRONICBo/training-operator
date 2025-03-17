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
from kubeflow.trainer.models.io_k8s_api_core_v1_container_state import IoK8sApiCoreV1ContainerState
from kubeflow.trainer.models.io_k8s_api_core_v1_container_user import IoK8sApiCoreV1ContainerUser
from kubeflow.trainer.models.io_k8s_api_core_v1_resource_requirements import IoK8sApiCoreV1ResourceRequirements
from kubeflow.trainer.models.io_k8s_api_core_v1_resource_status import IoK8sApiCoreV1ResourceStatus
from kubeflow.trainer.models.io_k8s_api_core_v1_volume_mount_status import IoK8sApiCoreV1VolumeMountStatus
from kubeflow.trainer.models.io_k8s_apimachinery_pkg_api_resource_quantity import IoK8sApimachineryPkgApiResourceQuantity
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApiCoreV1ContainerStatus(BaseModel):
    """
    ContainerStatus contains details for the current status of this container.
    """ # noqa: E501
    allocated_resources: Optional[Dict[str, IoK8sApimachineryPkgApiResourceQuantity]] = Field(default=None, description="AllocatedResources represents the compute resources allocated for this container by the node. Kubelet sets this value to Container.Resources.Requests upon successful pod admission and after successfully admitting desired pod resize.", alias="allocatedResources")
    allocated_resources_status: Optional[List[IoK8sApiCoreV1ResourceStatus]] = Field(default=None, description="AllocatedResourcesStatus represents the status of various resources allocated for this Pod.", alias="allocatedResourcesStatus")
    container_id: Optional[StrictStr] = Field(default=None, description="ContainerID is the ID of the container in the format '<type>://<container_id>'. Where type is a container runtime identifier, returned from Version call of CRI API (for example \"containerd\").", alias="containerID")
    image: StrictStr = Field(description="Image is the name of container image that the container is running. The container image may not match the image used in the PodSpec, as it may have been resolved by the runtime. More info: https://kubernetes.io/docs/concepts/containers/images.")
    image_id: StrictStr = Field(description="ImageID is the image ID of the container's image. The image ID may not match the image ID of the image used in the PodSpec, as it may have been resolved by the runtime.", alias="imageID")
    last_state: Optional[IoK8sApiCoreV1ContainerState] = Field(default=None, description="LastTerminationState holds the last termination state of the container to help debug container crashes and restarts. This field is not populated if the container is still running and RestartCount is 0.", alias="lastState")
    name: StrictStr = Field(description="Name is a DNS_LABEL representing the unique name of the container. Each container in a pod must have a unique name across all container types. Cannot be updated.")
    ready: StrictBool = Field(description="Ready specifies whether the container is currently passing its readiness check. The value will change as readiness probes keep executing. If no readiness probes are specified, this field defaults to true once the container is fully started (see Started field).  The value is typically used to determine whether a container is ready to accept traffic.")
    resources: Optional[IoK8sApiCoreV1ResourceRequirements] = Field(default=None, description="Resources represents the compute resource requests and limits that have been successfully enacted on the running container after it has been started or has been successfully resized.")
    restart_count: StrictInt = Field(description="RestartCount holds the number of times the container has been restarted. Kubelet makes an effort to always increment the value, but there are cases when the state may be lost due to node restarts and then the value may be reset to 0. The value is never negative.", alias="restartCount")
    started: Optional[StrictBool] = Field(default=None, description="Started indicates whether the container has finished its postStart lifecycle hook and passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. In both cases, startup probes will run again. Is always true when no startupProbe is defined and container is running and has passed the postStart lifecycle hook. The null value must be treated the same as false.")
    state: Optional[IoK8sApiCoreV1ContainerState] = Field(default=None, description="State holds details about the container's current condition.")
    user: Optional[IoK8sApiCoreV1ContainerUser] = Field(default=None, description="User represents user identity information initially attached to the first process of the container")
    volume_mounts: Optional[List[IoK8sApiCoreV1VolumeMountStatus]] = Field(default=None, description="Status of volume mounts.", alias="volumeMounts")
    __properties: ClassVar[List[str]] = ["allocatedResources", "allocatedResourcesStatus", "containerID", "image", "imageID", "lastState", "name", "ready", "resources", "restartCount", "started", "state", "user", "volumeMounts"]

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
        """Create an instance of IoK8sApiCoreV1ContainerStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in allocated_resources (dict)
        _field_dict = {}
        if self.allocated_resources:
            for _key_allocated_resources in self.allocated_resources:
                if self.allocated_resources[_key_allocated_resources]:
                    _field_dict[_key_allocated_resources] = self.allocated_resources[_key_allocated_resources].to_dict()
            _dict['allocatedResources'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in allocated_resources_status (list)
        _items = []
        if self.allocated_resources_status:
            for _item_allocated_resources_status in self.allocated_resources_status:
                if _item_allocated_resources_status:
                    _items.append(_item_allocated_resources_status.to_dict())
            _dict['allocatedResourcesStatus'] = _items
        # override the default output from pydantic by calling `to_dict()` of last_state
        if self.last_state:
            _dict['lastState'] = self.last_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict['resources'] = self.resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in volume_mounts (list)
        _items = []
        if self.volume_mounts:
            for _item_volume_mounts in self.volume_mounts:
                if _item_volume_mounts:
                    _items.append(_item_volume_mounts.to_dict())
            _dict['volumeMounts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoK8sApiCoreV1ContainerStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allocatedResources": dict(
                (_k, IoK8sApimachineryPkgApiResourceQuantity.from_dict(_v))
                for _k, _v in obj["allocatedResources"].items()
            )
            if obj.get("allocatedResources") is not None
            else None,
            "allocatedResourcesStatus": [IoK8sApiCoreV1ResourceStatus.from_dict(_item) for _item in obj["allocatedResourcesStatus"]] if obj.get("allocatedResourcesStatus") is not None else None,
            "containerID": obj.get("containerID"),
            "image": obj.get("image") if obj.get("image") is not None else '',
            "imageID": obj.get("imageID") if obj.get("imageID") is not None else '',
            "lastState": IoK8sApiCoreV1ContainerState.from_dict(obj["lastState"]) if obj.get("lastState") is not None else None,
            "name": obj.get("name") if obj.get("name") is not None else '',
            "ready": obj.get("ready") if obj.get("ready") is not None else False,
            "resources": IoK8sApiCoreV1ResourceRequirements.from_dict(obj["resources"]) if obj.get("resources") is not None else None,
            "restartCount": obj.get("restartCount") if obj.get("restartCount") is not None else 0,
            "started": obj.get("started"),
            "state": IoK8sApiCoreV1ContainerState.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "user": IoK8sApiCoreV1ContainerUser.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "volumeMounts": [IoK8sApiCoreV1VolumeMountStatus.from_dict(_item) for _item in obj["volumeMounts"]] if obj.get("volumeMounts") is not None else None
        })
        return _obj


