from time import sleep
from whatsapp_api_JPO import WhatsApp_JPO
from RandomDraw import draw

groupName = 'Todos os migues do'
groupName = 'João Paulo Bot'
msg = "Olá, aqui é o Jonas' bot."
eu = 'João Paulo Bot'

# Starting Chrome session:
wp = WhatsApp_JPO()                     # Abre Chrome já na página do WhatsApp Web.
input('Press after QR code scan.')      # Waiting for QR code scan.

# Getting list of participants from group:
wp.search_contact(groupName)            # Procura por nome ou número do contato (ou nome do grupo). Se houver homônimos, retorna o primeiro.
sleep(3)
participants = wp.get_group_members_long()   # Getting everybody's numbers
# print(participants)

# Making the draw:
drawn = draw(participants)
for i in range(len(drawn)):     # Substituting "Você". Will send msg to individual group.
    if drawn[i] == 'Você':
        drawn[i] = eu
# print(drawn)
print('The drawn was done!')

# Sending drawn person for each contact:
for i in range(len(drawn)-1):

    wp.search_contact(drawn[i])                                     # Search contact.
    sleep(1)
    msg2 = 'No amigo oculto, você presenteará ' + drawn[i+1]        # Building message to send.
    wp.send_message(msg)                                            # Sending message.
    wp.send_message(msg2)                                           # Sending message.
    sleep(1)

    if drawn[i] != eu:                                              # If message was to sent to me,
        wp.delete_message_from_recent(msg2)                         # Deletes sent message (only for bot, not for recipient)