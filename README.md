Repo used by Data team to extract data in a Meltano pipeline from Purecloud, the
telephone system for UK.

Below is original readme of this repo but note it may be out of date. This is a fork
of [this repo](https://github.com/rumeau/tap-purecloud) from user rumeau. That is
itself a fork of the [original repo](https://github.com/singer-io/tap-purecloud)
from Drew Banin.

Forked from the remeau repo to allow bug fixes and controlling the version we use as
Meltano just pulls the latest version from master.

-----------------

# tap-purecloud

Author: Drew Banin (drew@fishtownanalytics.com)

This is a [Singer](https://singer.io) tap that produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:
 - Pulls data from the [PureCloud API](https://developer.mypurecloud.com/api/rest/v2/)
 - Fetches the following resources:
   - [users](https://developer.mypurecloud.com/api/rest/v2/users/index.html#getUsers)
   - [groups](https://developer.mypurecloud.com/api/rest/v2/groups/index.html#getGroups)
   - [locations](https://developer.mypurecloud.com/api/rest/v2/locations/index.html#getLocations)
   - [presence definitions](https://developer.mypurecloud.com/api/rest/v2/presence/index.html#getPresencedefinitions)
   - [queues](https://developer.mypurecloud.com/api/rest/v2/routing/index.html#getRoutingQueues)
    - [queue membership](https://developer.mypurecloud.com/api/rest/v2/routing/index.html#getRoutingQueuesQueueIdUsers)
    - [queue wrapup codes](https://developer.mypurecloud.com/api/rest/v2/routing/index.html#getRoutingQueuesQueueIdWrapupcodes)
   - [management units](https://developer.mypurecloud.com/api/rest/v2/workforcemanagement/index.html#getWorkforcemanagementManagementunits)
    - [activity codes](https://developer.mypurecloud.com/api/rest/v2/workforcemanagement/index.html#getWorkforcemanagementManagementunitsMuIdActivitycodes)
    - [schedules (with a configurable lookahead)](https://developer.mypurecloud.com/api/rest/v2/workforcemanagement/index.html#postWorkforcemanagementManagementunitsMuIdSchedulesSearch)
    - [historical adherence](https://developer.mypurecloud.com/api/rest/v2/workforcemanagement/index.html#postWorkforcemanagementAdherenceHistorical)
   - [conversations](https://developer.mypurecloud.com/api/rest/v2/conversations/index.html)
   - [user details](https://developer.mypurecloud.com/api/rest/v2/users/index.html#getUsersUserIdProfile)

## Quick Start
#### 1. Create and source a virtualenv

```
$ virtualenv env
$ source env/bin/activate
```

#### 2. Install from source

```
$ pip install .
```

#### 3. Create a config file

You must create a JSON configuration file that looks like this:

```json
{
    "domain": "mypurecloud.ie",
    "client_id": "...",
    "client_secret": "...",
    "start_date": "2018-01-01",
    "schedule_lookahead_weeks": 5
}
```

You can find your Client ID and Client Secret in the Purecloud web interface. Note that depending
on your location, your domain may either be a `.ie` or `.com` domain.

#### 6. Run the tap

```
 tap-purecloud -c config.json -p catalog.json
```

The output of `tap-purecloud ...` can be piped to `target-stitch` to load the data into your warehouse.

---

Copyright &copy; 2018 Stitch
