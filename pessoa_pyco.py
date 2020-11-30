from psyco_connection import cursor


def insere_pessoa(dados_pessoa):
    cursor.execute("INSERT INTO pessoa (name, endereco, cpf, estado,"
                   "turma, periodo, modulo)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (
                       dados_pessoa['name'],
                       dados_pessoa['endereco'],
                       dados_pessoa['cpf'],
                       dados_pessoa['estado'],
                       dados_pessoa['turma'],
                       dados_pessoa['periodo'],
                       dados_pessoa['modulo']
                   )
                   )


def retorna_pessoas():
    cursor.execute("SELECT * FROM pessoa")
    return cursor.fetchall()


def retorna_pessoa(id):
    cursor.execute("SELECT * FROM pessoa WHERE id = %s", [id])
    pessoa = cursor.fetchone()
    return pessoa


def atualiza_pessoa(pessoa):
    query = "UPDATE pessoa SET name = %s, endereco = %s, cpf = %s, estado = %s, turma = %s, periodo = %s, modulo = %s" \
            "WHERE id = %s"
    params = [pessoa['name'], pessoa['endereco'], pessoa['cpf'], pessoa['uf'], pessoa['turma'], pessoa['periodo'],
              pessoa['modulo'], pessoa['id']]

    cursor.execute(query, params)


def remove_pessoa(id):
    cursor.execute("DELETE FROM pessoa WHERE id = %s", [id])
