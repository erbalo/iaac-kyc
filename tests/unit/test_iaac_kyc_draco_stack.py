import aws_cdk as core
import aws_cdk.assertions as assertions

from infra.iaac_kyc_draco_stack import IaacKycDracoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in iaac_kyc_draco/iaac_kyc_draco_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = IaacKycDracoStack(app, "iaac-kyc-draco")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
