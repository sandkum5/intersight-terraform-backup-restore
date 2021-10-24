.DEFAULT_GOAL = run

.PHONY: run tfrun parser

run: tfrun parser

tfrun: main.tf
	@echo "Start Terraform workflow"
	terraform init
	terraform apply -auto-approve
	@echo "End Terraform workflow"

parser: terraform.tfstate
	@echo "Start terraform state parser"
	python ntp_policy_parser.py
	@echo "End terraform state parser"
