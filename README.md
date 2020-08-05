Archiware P5 Module
====================

Reports Archiware P5 client data to MunkiReport.

![](https://github.com/CristianNic/archiware_p5/blob/master/listing.jpg)

Notes
-----

Archiware provides data management software for backup, synchronization & archiving for small-medium sized businesses & the media/entertainment industry.

https://www.archiware.com/

Table Schema
-----

* host_id         - VARCHAR(255) - Client ID number
* port            - Integer      - Port Server is running on
* platform        - VARCHAR(255) - Platform client is running on (linux, freeBSD, windows, macOS)
* p5_version      - VARCHAR(255) - P5 software Version
* uptime          - VARCHAR(255) - Amount of time P5 software has been running
* archive_plan    - VARCHAR(255) - If ArchivePlan is licensed and amount of licenses available
* backup_plan     - VARCHAR(255) - If BackupPlan is licensed and amount of licenses available
* sync_plan       - VARCHAR(255) - If SyncPlan is licensed and amount of licenses available  
* backup2go       - VARCHAR(255) - If Backup2Go is licensed and amount of licenses available
* client          - VARCHAR(255) - If Client is licensed and amount of licenses available
* thin_client     - VARCHAR(255) - If ThinClient is licensed and amount of licenses available
* virtual_client  - VARCHAR(255) - If VirtClient is licensed and amount of licenses available
* device          - VARCHAR(255) - If Device is licensed and amount of licenses available
* jukebox         - VARCHAR(255) - If Jukebox is licensed and amount of licenses available
* desktop_links   - VARCHAR(255) - If Archive App is installed and amount of licenses available


