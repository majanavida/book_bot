LEXICON: dict[str, str] = {
    'forward': '>>',
    'backward': '<<',
    '/start': ('<b>Привет!</b>\n'
               'Это бот, в котором ты сможешь прочитать книгу '
               'Фридриха Ницше "По ту сторону добра и зла"\n'
               'Чтобы посмотреть все доступные команды, напиши /help'),
    '/help': ('<b>Это бот-книжка</b>\n'
              'Список доступных команд:\n'
              '/beginning - в начало книги\n'
              '/continue - продолжить чтение\n'
              '/bookmarks -  посмотреть список своих закладок\n'
              'Чтобы создать закладку - нажмите на кнопку с номером страницы'),
    '/bookmarks': '<b>Список ваших закладок:</b>',
    'edit_bookmarks': '<b>Редактировать закладки</b>',
    'edit_bookmarks_button': '🗑️ Редактировать',
    'del': '🗑️',
    'cancel': '🗙 Отменить',
    'no_bookmarks': ('У вас пока нет закладок.\n'
                     'Чтобы создать закладку - '
                     'нажмите на кнопку с номером страницы'),
    'cancel_text': '/continue - продолжить чтение',
}


LEXICON_COMMANDS: dict[str, str] = {
    '/beginning': 'В начало книги',
    '/continue': 'Продолжить чтение',
    'bookmarks': 'Закладки',
    '/help': 'Справка по работе бота',
}