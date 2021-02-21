if [ ! -f .initialized ]; then
    echo "Initializing container"
    python code/modules/import.py
    touch .initialized
fi

exec "$@"