#!/bin/bash

# jpy_start - Start a Jupyter Notebook server with options

start_jupyter() {
    local port=8888

    while [[ $# -gt 0 ]]; do
        case "$1" in
            -p|--port)
                if [[ -n "$2" && "$2" =~ ^[0-9]+$ ]]; then
                    port="$2"
                    shift 2
                else
                    echo "Error: --port requires a numeric argument." >&2
                    exit 1
                fi
                ;;
            -h|--help)
                echo "Usage: jpy_start [OPTIONS]"
                echo ""
                echo "Options:"
                echo "  -p, --port <PORT>     Specify the port to run Jupyter on (default: 8888)"
                echo "  -h, --help            Show this help message and exit"
                exit 0
                ;;
            *)
                echo "Unknown option: $1" >&2
                echo "Use --help to see available options." >&2
                exit 1
                ;;
        esac
    done

    echo "Starting Jupyter Notebook on port $port..."
    jupyter notebook --port="$port"
}

# Entry point
start_jupyter "$@"
