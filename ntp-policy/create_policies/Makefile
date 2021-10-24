.DEFAULT_GOAL = run

.PHONY: run tfrun

run: tfrun

tfrun: main.tf
	@echo "Start Terraform workflow"
	terraform init
	terraform apply -auto-approve -var-file=../get_policies/terraform.tfvars.json
	@echo "End Terraform workflow"
