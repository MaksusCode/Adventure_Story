
# Вы можете расположить сценарий своей игры в этом файле.




# Определение персонажей игры.

define r = Character('Рафталия', color="#f97306")
define n = Character('Наофуми', color = "#c8ffc8")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:

label start:

    $ unkn_name = "?????"

    $ check_ques = 0


    scene bg time_left

    unkn_name "Эй, вставай чего разлегся?"
    unkn_name "Эй, ты вообще меня слышишь?"


    scene bg forest
    with Dissolve(.5)

    show raftalia stay

    unkn_name "О, очнулся, хотелось бы мне знать кто ты такой"
    unkn_name "Но сейчас это не особо важно"
    unkn_name "Ты ж не местный я права?"
    
    

    r "Я [r]"
    r "Что ты здесь делаеш?"


    "Мне нужно в деревню, и найти там старейшину"

    r "Так ты знаеш где тут деревня?"

    menu:

        "Да.":
            jump question_choise_yes

        "Нет":
            jump question_choise_passive
        
        "Как нибудь розберусь отвали от меня":
            jump question_choise_angry


    label question_choise_yes:

        show raftalia smile

        r "Хмм..."
        r "Хотелось бы знать откуда?"
        r "Просто я тебя раньше здесь не видела"
        r "Ну как бы там не было удачи!"
        show raftalia stay
        r "Стой, подожди."
        "Что такое?"
        r "Как тебя зовут?"
        python:
            name_player = renpy.input("Как вас зовут?")
        r "Удачи [name_player]"
        scene bg exit_forest
        with Dissolve(.5)

        "Вот и выход, надо идти к тому старику который управляет всей этой деревней"
        "И спросить что он от меня хотел"

        scene bg enter_village
        with Dissolve(.5)

        "Так, вот эта самая деревня"
        "Насколько я помню старик большую часть времени в Южной части деревни"
        "Она же \"Золотая\", одни работают в поле, а другие сидят в своих роскошних домах и смотрят как работают другие"
        "Мда нужно идти"

        jump Midle_Village


    
    label question_choise_angry:

        show raftalia sad

        r "Ноо..."
        r "Я ведь хотела только помочь"
        r "Ну и броди здесь, раз не хочеш что-бы тебе помогали"
        

    label question_choise_passive:

        show raftalia stay

        r "Смотри: Идеш по этой тропе и когда увидеш большое дерево рядом с колонами, сворачиваеш налево"
        show raftalia smile
        r "Ну надеюсь ты понял."

        scene bg forest2
        with Dissolve(.5)

        "Так..."
        "Она сказала идти по этой тропе но..."
        "Где она вообще увидела здесь тропу!?"
        "Ну ладно, надо идти дальше."

        scene bg time_left
        with Dissolve(.5)


        "Прошло 2 часа"


        scene bg big_tree
        with Dissolve(.5)
        "Кажется это здесь"
        "Но куда она говорила, надо сворачивать?"
        "Я столько искал это место, что уже все забыл"
        "Так... И куда же мне пойти?"
        
        menu:

            "Направо.":
                "\"Иди направо, когда увидеш огромное дерево\""
                "Да именно так она и сказала"

                jump turn_right


            "Налево": 
                
                "Вроде бы она говорила сворачивать налево"

                jump turn_left

        
        label turn_right:

            scene bg forest3
            with Dissolve(.5)

            "Хмм... А я точно правильно пошел?"
            "Потому что здесь нет не деревни, некакого либо человека"

            scene bg forest4
            with Dissolve(.5)

            "Вот блин это снова она"
            "Черт по-моему я заблудился"

            show raftalia stay

            r "И что ты тут делаеш?"
            r "Я ж сказала тебе свернуть налево!"
            r "Ну раз ты уже здесь, то я тебя проведу"
            r "И кстати, как хоть тебя зовут?"

            python:
                name_player = renpy.input("Как вас зовут?")
            

            r "[name_player] значит, да?"

            scene bg enter_village
            with Dissolve(.5)

            name_player "Ну вот и она."

            r "А? ты что-то сказал"

            name_player "Говорю вот та самая деревня, наконец-то я здесь"

            show naofumi stay

            unkn_name "О, Рафталия, привет, а это кто?"
            
            hide naofumi
            show raftalia smile 
            
            r "[n], привет, это [name_player] он пришел в деревню, что-бы найди старейшину"

            hide raftalia
            show naofumi stay

            n "[name_player], да?"
            n "Будем знакомы, я [n]"
            n "Старейшина сейчас скорее всего в Южной части деревни"

            name_player "Спасибо, я пойду"

            hide naofumi
            show raftalia smile

            r "Удачи!"

            jump Midle_Village


        label turn_left:

            scene bg exit_forest
            with Dissolve(.5)

            "фух... Я действительно нашел этот выход"
            "Черт я был в этом лесу раньше, но почему же я тогда заблудился?"

            scene bg enter_village
            with Dissolve(.5)


            "Это и есть та самая деревня"
            "как и говорила та незнакомка"
            "Как её там Раф... Рафтал... Что-то там"

            show naofumi stay

            unkn_name "А? ты кто я тебя здесь раньше не видел"
            unkn_name "Как тебя зовут?"

            python:
                name_player = renpy.input("Как вас зовут?")
            
            
            unkn_name "Хмм... [name_player] я тебя раньше не видел"
            name_player "Какая-то девушка в лесу помогла мне выйти из леса я ищю старика"

            unkn_name "А, не [r] случаем?"
            unkn_name "Стоп ты сказал старика?"
            unkn_name "Что за старик?"
            
            name_player "Точно, [r], так она представилась."
            name_player "А, старик это старейшина этой деревни"
            
            unkn_name "Так ты ищешь старейшину да?"
            
            name_player "Да, а ты случаем не знаеш где его найти?"
            name_player "И кстати я так и не спросил твоего имени."

            unkn_name "А прости за мою грубость"
            n "Моё имя [n]"

            n "Старейшина скорее всего в Южной части деревни"

            name_player "Мда..."
            name_player "Как я и думал"

            n "Так ты знаеш его?"

            name_player "Да, мы знакомы"
            n "Значит ты знаеш куда идти"
            n "Ну тогда удачи, [name_player]."

            name_player "Да, спасибо"
            jump Midle_Village
            

    label Midle_Village:
        
        scene bg village2
        with Dissolve(.5)

        name_player "Мда здесь люди работают на полях, а куда я сейчас иду совсем другая обстановка"
        name_player "Люди сидят в своих роскошных домах, и просто смотрят как работают другие"
        name_player "Но старик не такой, деньги не смогут его поменять"




    return
