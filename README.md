## Dockerised sickbeard_mp4_automator

This docker container uses python XML RPC to allow you to use sickbeard_mp4_automator from outside the container.

### Key configuration items

- Default port is 7784
- Config file is stored in volume at `/config`
- File storage is in volume at `/files`

### How to use

1. Start docker container, with appropriate ports exposed and above volumes pointed at the correct places
2. Copy the `call.py` script from the repository (https://github.com/mrkno/docker_sma) into the appropriate folder (in place of the one you would usually copy, e.g `postProcessRadarr.py`).
3. Run `call.py` once to get a configuration file. Update the configuration parameters to point at your docker container and to remap file paths as appropriate.
4. Follow normal config process from here.

### Why would I use this?

This container allows you to keep the processing of files containerised and means that you do not have to install dependencies on the host. This has security and ease of installation advantages.

