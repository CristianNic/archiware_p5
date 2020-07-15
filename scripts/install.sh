#!/bin/bash

# archiware_p5 controller
CTL="${BASEURL}index.php?/module/archiware_p5/"

# Get the scripts in the proper directories
"${CURL[@]}" "${CTL}get_script/archiware_p5.py" -o "${MUNKIPATH}preflight.d/archiware_p5.py"

# Check exit status of curl
if [ $? = 0 ]; then
	# Make executable
	chmod a+x "${MUNKIPATH}preflight.d/archiware_p5.py"

	# Set preference to include this file in the preflight check
	setreportpref "archiware_p5" "${CACHEPATH}archiware_p5.json"

else
	echo "Failed to download all required components!"
	rm -f "${MUNKIPATH}preflight.d/archiware_p5.py"

	# Signal that we had an error
	ERR=1
fi
