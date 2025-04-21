echo "======================================================="
echo -e "${PURPLE} [3] Postgres SQL database. ${RESET}"

POSTGRES_OUTPUT=$(mktemp)
POSTGRES_ERR=$(mktemp)

bash -c "sudo apt install postgresql-16" >"$POSTGRES_OUTPUT" 2>"$POSTGRES_ERR"
EXIT_CODE=$?

echo -e "${PURPLE} [3.1] Instalando o pacote de desenvolvimento do Postgres SQL. ${RESET}"
sudo apt install postgresql-server-dev-16

if [ $EXIT_CODE -ne 0 ]; then
    echo -e "${RED}  [❌] error postgresql ${RESET}"

    # TODO: Acredito q ele nao esteja caindo nessa condição
    if [[ $POSTGRES_ERR =~ "postgres.h: No such file or directory" ]]; then
        echo "yes error"
        echo -e "${PURPLE} [3.1] Instalando o pacote de desenvolvimento do Postgres SQL. ${RESET}"
        sudo apt install postgresql-server-dev-16
    fi

    # TODO: Acredito q ele nao esteja caindo nessa condição
    if [[ $POSTGRES_ERR =~ "fatal: destination path 'pgvector' already exists and is not an empty directory." ]] then
        echo -e "${GREEN}  [✅] postgresql db ja existe ${RESET}"
    fi
else
    echo -e "${GREEN}  [✅] postgresql db instalado com sucesso ${RESET}"
    echo "${POSTGRES_OUTPUT}"
fi