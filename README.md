# Akame Monitor

Akame Monitor is a collection of tools to constantly monitor web changes. It contains a couple of modules such as extraction, comparison, and notification and allows users to design their own units and flexibly construct the monitoring workflow.

- [Akame Monitor](#akame-monitor)
  - [Use Cases](#use-cases)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Extractor Sets Available](#extractor-sets-available)

## Use Cases

Akame Monitor can **monitor a web change every X seconds for Y rounds**. Specifically, some common tasks that Akame Monitor can handle are as follows:

- Extraction: Fetching the response from an API endpoint using a specific request header
- Comparison: Compare the latest API response against the previous version
- Notification: Send out a notification through [Pullover](https://pushover.net/) if there are changes between the monitored content

## Installation

```bash
# switch to the folder to save the script
# cd <target-download-folder>
git clone https://github.com/mcknote/AkameMonitor.git
```

## Usage

Follow these steps to use Akame Monitor:

1. Edit `AkameMonitor/config.json` with the monitoring task information
   - `task_name`: The name of this monitoring task; this will appear in the console logs and notification programs.
   - `target_url`: The URL to be monitored, e.g. an API endpoint or a webpage.
   - `exset_id`: The ID of Extractor Set, which handles both the URL and content extraction. Default to `BASIC`. See [Extractor Sets Available](##extractor-sets-available) for more details.
   - `loop_seconds`: The interval in seconds between all monitoring rounds. Default to 30 seconds.
   - `loop_max_rounds`: The maximum number of rounds to monitor. Default to 86400 rounds (so with 30 seceonds, this would make a one-month monitoring task).
2. Run `AkameMonitor/main.py` while keeping the process alive throughout the monitoring cycle

## Extractor Sets Available

| ID | Description | URL Base | Content Extractor |
| --- | --- | --- | --- |
| `BASIC` | The basic extractor set that fetches content directly from only the URL given. This set almost equates to a `request.get(target_url)` call. | `core.URLBase` | `basic.BasicExtractor` |
