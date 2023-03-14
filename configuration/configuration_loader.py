import re
import typing

from dynaconf import LazySettings
from infra.enums.types import Resource

settings = LazySettings(
    ROOT_PATH_FOR_DYNACONF="./configuration/"
)


class ConfigurationLoader:

    # TODO add validation for empty string
    @staticmethod
    def getSetting(setting_key: str):
        return settings[setting_key]


    # TODO add validation for empty string
    @staticmethod
    def build_naming_convention(convention: str):
        org = settings.ORG
        namespace = settings.NAMESPACE
        project_name = settings.PROJECT_NAME

        return f"{org}-{project_name}-{convention}-{namespace}"


    @staticmethod
    def build_resource_naming_convention(service_acronym: str, resource_name:str, resource: Resource, *, include_project_name: bool = False):
        org = settings.ORG
        namespace = settings.NAMESPACE
        project_name = settings.PROJECT_NAME
        project_name = re.sub('\s|\-', "_", project_name)
        resource_name = re.sub('\s|\-', "_", resource_name)
        service_acronym = re.sub('\s|\-', "_", service_acronym)

        if include_project_name:
            return f"{org}_{project_name}_{service_acronym}_{resource_name}_{resource.value}_{namespace}"
        else:
            return f"{org}_{service_acronym}_{resource_name}_{resource.value}_{namespace}"


    @staticmethod
    def build_out_naming_convention(convention: str):
        convention = re.sub('\s|\-|\_', ":", convention)
        org = settings.ORG
        namespace = settings.NAMESPACE
        project_name = settings.PROJECT_NAME

        return f"{org}:{project_name}:{convention}:{namespace}"


    @staticmethod
    def build_arn_convention(resource_type: Resource, resource: str, *, with_account: typing.Optional[str] = None, with_region: typing.Optional[str] = None):
        xstr = lambda s, default: default if s is None else s

        account = xstr(with_account, settings.AWS_ACCOUNT)
        region = xstr(with_region, settings.AWS_REGION)

        return f"arn:aws:{resource_type.value}:{region}:{account}:{resource}"