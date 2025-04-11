echo "Starting langfuse locally..."
cd ~
cd Desktop
cd langfuse
OUTPUT="$(sudo docker compose up)"
echo ">>>${OUTPUT}
