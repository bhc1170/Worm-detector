rule ExampleRule {
    meta:
        description = "Example rule to detect specific content"
        date = "2024-07-30"
    strings:
        $text_string = "malicious content"
        $hex_string = { E2 34 A1 C3 23 }
        $regex_string = /malware[0-9]+/
    condition:
        $text_string or $hex_string or $regex_string
}

