# Dynamic HTML

Description of the system

## To Deploy in Cloudformation

### 1- Permissions

Ensure that the user has the correct AWS permissions:

- CloudFormation full access
- IAM create role and policy permissions
- S3 full access
- API Gateway full access
- Lambda full access
- Systems Manager (SSM) Parameter Store access

You can see the aws_permissions_policy.json file as an example, ensure that the <account-id> value is set correctly

### 2- Stack Creation

Create the stack in a terminal executing the following command

> aws cloudformation create-stack --stack-name dynamic-html --template-body file://cloudformation_template.yaml --capabilities CAPABILITY_NAMED_IAM

### 3- Get the stack outputs

Get the outputs from the stack and get the ApiEndpoint Output value that you will replace in the index.html file.

This should be something like this where the key-value change between executions:

> aws cloudformation describe-stacks --stack-name dynamic-html --query 'Stacks[0].Outputs[]'

Example:
"OutputValue": "https://<key-value>.execute-api.us-east-1.amazonaws.com/prod/value",

### 4- Update the index.html file and upload it

Replace the <key-value> in the index.html file

Upload the file into the s3 bucket that was created ("dynamicstringbucket").

### 5- Use the output from the stack WebsiteURL to visit the Public URL

It should be something like this

"OutputValue": "http://dynamicstringbucket.s3-website-us-east-1.amazonaws.com"

### 6- Update the dynamic string

Each time a client execute the request to the url will receive the same output, but it can be change using the APIGateway Put method, in order to do that, use the update_string.py file to modify the "dynamic string" value.

Modify the file update_string.py with the correct <key-value> of the ApiEndpoint URL and the correct value message.

### 9- Check the changes

Reload the WebsiteURL page to see the new message.
