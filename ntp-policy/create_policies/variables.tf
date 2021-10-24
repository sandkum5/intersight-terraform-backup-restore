variable "ntp" {
    type = list(object({
        name = string
        description = string
        org_name = string
        ntp_policy_enabled = bool
        ntp_server_ips = list(string)
        ntp_policy_timezone = string
        tags = list(object({
            key = string
            value = string
            additional_properties = string
        }))
    }))
    default = [{
            name = "demo-ntp1"
            description = "DEMO NTP1 for SJ"
            ntp_policy_enabled = true
            org_name = "default"
            ntp_server_ips = ["1.1.1.1", "2.2.2.2"]
            ntp_policy_timezone = "America/Los_Angeles"
            tags = [{key = "Location", value = "SJ", additional_properties = ""}]
        }]
    description = <<EOT
    name                : Name of NTP policy
    description         : Description of the NTP Policy
    org_name            : Organization Name
    ntp_policy_enabled  : If NTP Policy is enabled
    ntp_server_ips      : List of NTP servers
    ntp_policy_timezone : Timezone of the NTP policy
    tags                : Tags
    EOT
}