GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
RESET='\033[0m' # resets

echo "======================================================="
echo -e "${PURPLE} [1] Docker Setup. ${RESET}"

echo -e "  ${PURPLE}[1.1] Add docker's official GPG Key: ${RESET}"
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo -e "${PURPLE}  [1.2] Add the repository to Apt sources: ${RESET}"
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
echo -e "${PURPLE}  [1.3] Testing docker ${RESET}"

DOCKER_HELLO_WORLD=$(sudo docker run hello-world 2>&1)

if [ $? -ne 0 ]; then
    echo -e "${RED}  [❌] error ao executar docker run hello-world ${RESET}"
else
    echo -e "${GREEN}  [✅] Docker configurado com sucesso! ${RESET}"
fi

# ==============================================
# Ollama setup
# ==============================================
# chmod +X ./setup-ollama.sh
# source setup-ollama.sh 

# ==============================================
# PostgreSQL 16 Setup
# ==============================================
chmod +X ./setup-postgresql.sh
source setup-postgresql.sh

# ==============================================
# PGVector vectorial database Setup
# ==============================================
cd /tmp
git clone --branch v0.8.0 https://github.com/pgvector/pgvector.git
cd pgvector/
make
if sudo make install; then
    echo -e "${GREEN}  [✅] PGVector configurado com sucesso! ${RESET}"
else
    echo -e "${RED}  [❌] Error: PGVector. ${RESET}"
fi

# ==============================================
# Langfuse Setup
# ==============================================
echo "======================================================="
echo -e "${PURPLE} [] Langfuse self-hosted server. ${RESET}"

# Langfuse
cd ~
cd Desktop
git clone https://github.com/langfuse/langfuse.git
cd langfuse
echo -e "${PURPLE}  [.1] Start langfuse locally ${RESET}"
sudo docker compose up
