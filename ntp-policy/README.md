# NTP Policies

## Steps to execute

### STEP 1
#### Get Existing NTP Policies from all the Orgs in the Account.
1. Change to directory "get_policies".
2. Add Intersight API Key in provider.tf file for variable "apikey" and add SecretKey.txt file.
3. Execute "make". This should create a terraform.tfvars.json file.

### STEP 2
#### Create NTP Policies for all the Orgs in the new Account.
1. Change to directory "create_policies".
2. Add Intersight API Key in provider.tf file for variable "apikey" and add SecretKey.txt file.
3. Execute "make". This should create the policies in the new Account using terraform.tfvars.json file in get_policies directory.

# NOTE
*Ensure you provide API keys for a test account in STEP 2 to validate it works as expected.
*This will create the objects and can affect production.
*Don't run this against a production account unless you know what you are doing.