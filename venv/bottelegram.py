import telebot
import requests

CHAVE_API = "7689773573:AAGj-pwYLveXgb8WL_FwzLWOmXVn_hwT5o8"
BOOK_API = "AIzaSyBpFJMQC0nrz0OO0yQ-yFXu32T81qiKGfc"

bot = telebot.TeleBot(CHAVE_API)
# Armazena o estado atual da conversa
user_search_state = {}

# Comandos para a opção 1 (ficção)
@bot.message_handler(commands=['option1'])
def option1(message):
   texto = """
   Click on which genre you want to read:
   /Classics
   /Criminal
   /Fantasy
   /Horror
   /Romance
   /Poetry
   """
   bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=['Classics'])
def Classics(message):
    chat_id = message.chat.id
    with open('assets/orwell.jpg', 'rb') as george:
        caption = """✨ Enjoy your reading! ✨
    <a href='https://uk.bookshop.org/p/books/animal-farm-george-orwell/37710?aid=1178&ean=9780141036137'>Animal Farm</a> - George Orwell"""
        bot.send_photo(
            chat_id, 
            photo=george, 
            caption=caption,
            parse_mode="HTML"
        )

@bot.message_handler(commands=['Criminal'])
def Criminal(message):
    chat_id = message.chat.id
    with open('assets/stephen.jpg', 'rb') as stephenking:
        caption = """✨ Enjoy your reading! ✨
    <a href='https://uk.bookshop.org/p/books/holly-the-chilling-new-masterwork-from-the-no-1-sunday-times-bestseller-stephen-king/7416215?aid=121&ean=9781399712958'>Holly</a> - Stephen King"""
        bot.send_photo(
            chat_id, 
            photo=stephenking, 
            caption=caption,
            parse_mode="HTML"
        )

@bot.message_handler(commands=['Fantasy'])
def Fantasy(message):
    chat_id = message.chat.id
    with open('assets/thelibrary.jpg', 'rb') as huchu:
        caption = """✨ Enjoy your reading! ✨
    <a href='https://uk.bookshop.org/p/books/the-library-of-the-dead-t-l-huchu/1946697?ean=9781529039474'>The Library of the Dead</a> - T.L. Huchu"""
        bot.send_photo(
            chat_id, 
            photo=huchu, 
            caption=caption,
            parse_mode="HTML"
        )

@bot.message_handler(commands=['Horror'])
def Horror(message):
    chat_id = message.chat.id
    with open('assets/ghosts.jpg', 'rb') as ghosts:
        caption = """✨ Enjoy your reading! ✨
    <a href='https://uk.bookshop.org/p/books/city-of-ghosts-victoria-schwab/205542?aid=3007&ean=9781407192765'>City of Ghosts</a> - Victoria Schwab"""
        bot.send_photo(
            chat_id, 
            photo=ghosts, 
            caption=caption,
            parse_mode="HTML"
        )


# Comandos para a opção 2 (não-ficção)
@bot.message_handler(commands=['option2'])
def option2(message):
    texto = """
   ⚜ Click on which genre you want to read:
   /Education
   /HealthandFitness
   /History
   /Religion
   """
    bot.send_message(message.chat.id, texto)
   
@bot.message_handler(commands=['Education'])
def Education(message):
    chat_id = message.chat.id
    with open('assets/freire.jpg', 'rb') as freire:
        caption = """✨ Enjoy your reading! ✨
<a href='https://uk.bookshop.org/p/books/pedagogy-of-the-oppressed-paulo-freire/3823089?aid=11660&ean=9780241301111'>Pedagogy of the Oppressed</a> - Paulo Freire"""
        bot.send_photo(
            chat_id, 
            photo=freire, 
            caption=caption,
            parse_mode="HTML"
        )
        
@bot.message_handler(commands=['HealthandFitness'])
def HealthandFitness(message):
    chat_id = message.chat.id
    with open('assets/health.jpg', 'rb') as health:
        caption = """✨ Enjoy your reading! ✨
<a href='https://uk.bookshop.org/p/books/the-mindful-body-thinking-our-way-to-chronic-health-ellen-langer/7426683?aid=12828&ean=9781472148612'>The Mindful Body</a> - Ellen Langer"""
        bot.send_photo(
            chat_id, 
            photo=health, 
            caption=caption,
            parse_mode="HTML"
        )

@bot.message_handler(commands=['History'])
def History(message):
    chat_id = message.chat.id
    with open('assets/history.jpg', 'rb') as history:
        caption = """✨ Enjoy your reading! ✨
<a href='https://uk.bookshop.org/p/books/one-fine-day-matthew-parker/4957549?aid=28&ean=9780349142364'>One Fine Day: Britain's Empire on the Brink</a> - Matthew Parker"""
        bot.send_photo(
            chat_id, 
            photo=history, 
            caption=caption,
            parse_mode="HTML"
        )

@bot.message_handler(commands=['Religion'])
def Religion(message):
    chat_id = message.chat.id
    with open('assets/religion.jpg', 'rb') as religion:
        caption = """✨ Enjoy your reading! ✨
<a href='https://uk.bookshop.org/p/books/lao-tzu-tao-te-ching-a-book-about-the-way-and-the-power-of-the-way-ursula-k-le-guin/4364056?ean=9781611807240'>Lao Tzu: Tao Te Ching</a> - Ursula K. Le Guin"""
        bot.send_photo(
            chat_id, 
            photo=religion, 
            caption=caption,
            parse_mode="HTML"
        )


# Comandos para a opção 3 (infantil)
@bot.message_handler(commands=['option3'])
def option3(message):
    texto = """
   ⚜ Click on which genre you want to read:
   /Pre-School
   /Poetry
   /Teen and Young Adult
   """
    bot.send_message(message.chat.id, texto)


# Comandos para a opção 4 (livros do mês)
@bot.message_handler(commands=['option4'])
def option4(message):
    texto = """
    ⚜ Click on which genre you want to read:
    
    """
    bot.send_message(message.chat.id, texto)
    pass


# Comandos para a opção 5 (buscar)
@bot.message_handler(commands=['option5'])
def option5(message):
    bot.send_message(
        message.chat.id,
        "⚜ Type in the title, author or publisher you want to search for:"
    )
    user_search_state[message.chat.id] = "waiting_for_search" # Define o estado do usuário como "esperando busca"
    
# Processa a resposta do usuário e busca os resultados
@bot.message_handler(func=lambda message: user_search_state.get(message.chat.id) == "waiting_for_search")
def search_books(message):
    search_query = message.text.lower() # Entrada do usuário para a busca
    results = search_in_database(search_query) # Função para buscar em uma "base de dados"

    if results:
        response = "Here are the results:\n" + "\n".join(results)
    else:
        response = "No results found for '{}'.".format(search_query)
        
    bot.send_message(message.chat.id, response)
    user_search_state[message.chat.id] = None # Redefine o estado após a busca

# Simula uma função que busca em uma base de dados
def search_in_database(query):
    # URL da API com a busca e a chave de API
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={BOOK_API}'
    
    # Realiza a requisição á API
    response = requests.get(url)
    
    # Converte a resposta para JSON
    data = response.json()
    
    #Verifica se há resultados
    if 'items' in data:
        results = []
        for item in data['items']:
            bookInfo = item['volumeInfo']
            title = bookInfo.get('title', 'Title not available.')
            authors = ', '.join(bookInfo.get('authors', ['Author unknown.']))
            publisher = bookInfo.get('publisher', 'Publisher not available.')
    
            result = f'▪ Title: {title} - Authors: {authors}, Publisher: {publisher}' + '\n'
            results.append(result)
        return results
    else:
        return ['No books found! Try again ✨']


# Resposta padrão
def verificar(mensagem):
        return True

@bot.message_handler(func=verificar)
def main(mensagem):
    texto = """
    ⚜ Choose an option below (click on the item):
    /option1 Fiction 
    /option2 Non-Fiction
    /option3 Children's
    /option4 Books of The Month
    /option5 Search titles, authors and Publishers"""
    bot.send_message(mensagem.chat.id, texto)

# Loop 
bot.infinity_polling()