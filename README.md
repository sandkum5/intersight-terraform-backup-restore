# intersight-terraform-backup-restore
- Repo to backup Orgs, Policies, Pools, Profiles etc using Terraform. 
- Create the objects under a different account or recreate in the same account using Terraform.  

### WORKFLOW
- Get existing objects using Terraform. 
- Use terraform.tfstate to create the terraform.tfvars.json file. 
- terraform.tfstate parsing and terraform.tfvars.json file creation is done using Python. 
- Created terraform.tfvars.json file is used to recreate the objects. 

### Following Objects workflow exists

#### NTP-Policy 
- Backup and Create NTP Policy. Review README.md in NTP-Policy director for more info. 

- More to come.. 
