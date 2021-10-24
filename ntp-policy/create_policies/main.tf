resource "intersight_ntp_policy" "ntp_policy" {
    for_each = {for ntp in var.ntp: ntp.name => ntp}
    name        = each.value.name
    description = each.value.description
    organization {
        object_type = "organization.Organization"
        selector = "$filter=Name eq '${each.value.org_name}'"
    }
    enabled = each.value.ntp_policy_enabled
    ntp_servers = each.value.ntp_server_ips
    timezone = each.value.ntp_policy_timezone
}