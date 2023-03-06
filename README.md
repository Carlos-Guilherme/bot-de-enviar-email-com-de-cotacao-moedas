# bot-de-enviar-email-com-de-cotacao-moedas

Este código Python é um exemplo de como automatizar o envio de e-mails com informações atualizadas sobre a cotação de moedas.

O programa utiliza algumas bibliotecas padrão do Python, como a "smtplib" para enviar e-mails, "email.message" para construir o corpo da mensagem e "datetime" e "time" para trabalhar com a data e hora atual.

A função "enviar_email()" é responsável por construir o corpo do e-mail, definir os cabeçalhos (assunto, remetente e destinatário), adicionar o conteúdo e enviar o e-mail através do servidor SMTP do Gmail.

Em seguida, o código define o horário de execução para 7:00 (horário definido pelo usuário) e entra em um loop infinito. A cada iteração, o código verifica se a hora atual é igual ao horário de execução. Se sim, ele realiza uma requisição na API AwesomeAPI, que retorna informações atualizadas sobre a cotação do dólar, euro e bitcoin em relação ao real brasileiro. Em seguida, ele chama a função "enviar_email()" para enviar um e-mail contendo as informações atualizadas da cotação das moedas.

Por fim, o programa espera por 60 segundos antes de verificar novamente se o horário atual é igual ao horário de execução, mantendo assim o loop em execução.
