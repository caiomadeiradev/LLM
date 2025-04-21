echo "======================================================="
echo -e "${PURPLE} [2] Ollama Self-hosted server. ${RESET}"

echo "Verificando drivers da NVIDIA..."
nvidia-smi

OLLAMA_OUTPUT=$(mktemp)
OLLAMA_ERR=$(mktemp)

bash -c "curl -fsSL https://ollama.com/install.sh | sh" >"$OLLAMA_OUTPUT" 2>"$OLLAMA_ERR"
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    echo -e "${RED}  [❌] error ao executar: OLLAMA_SELF_HOSTED ${RESET}"
    cat "${OLLAMA_ERR}"

    # Nvidia GPU Error
    if [[ $OLLAMA_ERR =~ "NVIDIA GPU detected" ]]; then
        echo -e "${PURPLE} [2.1] NVIDIA GPU Drivers setup. ${RESET}"
        echo -e "${PURPLE} Limpando as instalações anteriores... ${RESET}"
        sudo apt-get purge nvidia*
        sudo apt-get autoremove
        echo -e "${PURPLE} [2.2] Adicionando o repositório da NVIDIA... ${RESET}"
        sudo add-apt-repository ppa:graphics-drivers/ppa -y
        sudo apt-get update
        echo -e "${PURPLE} [2.3] Verificando os drivers recomendados... ${RESET}"
        ubuntu-drivers devices

        # O nvidia-driver-570 é especifico do meu PC (RTX 3070)
        sudo apt-get install nvidia-driver-570-server-open
        sudo reboot
    fi
else
    echo -e "${GREEN}  [✅] Sucesso! ${RESET}"
    echo "$OLLAMA_OUTPUT"
fi