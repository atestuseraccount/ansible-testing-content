#!/bin/bash

CHANGED="true"
MSG="hello from a module written in bash"
SOME_LIST='["blip", "foo", 37, 1.01, ""]'

printf '{"changed": %s, "msg": "%s", "contents": %s}' "${CHANGED}" "${MSG}" "${SOME_LIST}"
