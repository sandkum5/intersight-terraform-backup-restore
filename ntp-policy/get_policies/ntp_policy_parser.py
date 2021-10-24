#!/usr/bin/env python3
"""
    Script to parse Intersight Terraform State file.
    Write parsed objects to a yaml file.
    Use yaml file to recreate objects in Intersight.
"""

import json
from pprint import pprint

# Read file
def read_file(filename):
    """Read file"""
    with open(filename, "r") as f:
        tfstate_data = f.read()
    return tfstate_data


def org_parser(org_data_results):
    org_dict = {}
    for _, data in enumerate(org_data_results):
        org_name = data["name"]
        org_moid = data["moid"]
        org_dict[org_moid] = org_name
    return org_dict


def ntp_parser(ntp_data_results):
    ntp_data_dict = {"ntp": []}
    for x, data in enumerate(ntp_data_results):
        description = data["description"]
        name = data["name"]
        enabled = data["enabled"]
        timezone = data["timezone"]
        org_moid = data["organization"][0]["moid"]
        ntp_servers = data["ntp_servers"]
        tags = data["tags"]
        profiles = data["profiles"]
        ntp_object = {
            "description": description,
            "name": name,
            "org_moid": org_moid,
            "ntp_policy_enabled": enabled,
            "ntp_policy_timezone": timezone,
            "ntp_server_ips": ntp_servers,
            "profiles": profiles,
            "tags": tags,
        }
        ntp_data_dict["ntp"].append(ntp_object)
        # print(x+1, data['name'], data['ntp_servers'], data['timezone'])
    return ntp_data_dict


def main():
    filename = "terraform.tfstate"
    tfstate_data = read_file(filename)
    jsonData = json.loads(tfstate_data)

    # Get ntp and org data
    for _, data in enumerate(jsonData["resources"]):
        if data["type"] == "intersight_ntp_policy":
            ntp_data = data
        if data["type"] == "intersight_organization_organization":
            org_data = data

    ntp_data_results = ntp_data["instances"][0]["attributes"]["results"]
    org_data_results = org_data["instances"][0]["attributes"]["results"]

    org_dict = org_parser(org_data_results)
    ntp_data_dict = ntp_parser(ntp_data_results)

    # Update ntp_data_dict with org_name
    for item in ntp_data_dict["ntp"]:
        org_moid = item["org_moid"]
        if org_moid in org_dict.keys():
            item["org_name"] = org_dict[org_moid]
    pprint(ntp_data_dict)

    # Write parsed ntp_data_dict to json file used as terraform variable file
    with open("terraform.tfvars.json", "a") as f:
        json.dump(ntp_data_dict, f)


if __name__ == "__main__":
    main()
