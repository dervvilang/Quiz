def load_questions(filename):
    #загружает вопросы из файла.

    questions = [] #переменная для вопросов
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('#') or not line.strip():
                continue
            parts = line.strip().split(';') #переписываем строку для дольнейшей работы с ней (при вверном формате три части)
            if len(parts) == 3:
                question, options, answer = parts #вопрос, варианты ответа и ответ
                questions.append({
                    'question': question,
                    'options': options.split(','),
                    'answer': answer
                })
    return questions


def run_quiz(questions):
    #запускает викторину с заданными вопросами.

    correct_count = 0 #колво правильных ответов
    answers_report = [] #для хранения отчета

    for q in questions:
        print(q['question'])
        for i, option in enumerate(q['options']):
            print(f"{i + 1}. {option}")

        #контроль корректности ввода
        user_choice = None
        while True:
            try:
                user_choice = int(input('Ваш выбор: ')) - 1
                if 0 <= user_choice < len(q['options']):
                    break
                else:
                    print("Пожалуйста, введите корректный номер варианта.")
            except ValueError:
                print("Пожалуйста, введите число.")

        is_correct = q['options'][user_choice] == q['answer']
        if is_correct:
            correct_count += 1

        answers_report.append({
            'question': q['question'],
            'chosen': q['options'][user_choice],
            'correct': q['answer'],
            'is_correct': is_correct
        })

    #вывод правильных ответов в формате n/m
    total_questions = len(questions)
    print(f"\nВы ответили правильно на {correct_count} из {total_questions} вопросов.")

    #вывод отчетов для всех вопросов
    print("\nОтчет о прохождении теста:")
    for report in answers_report:
        print(f"Вопрос: {report['question']}")
        print(f"Ваш ответ: {report['chosen']}")
        print(f"Правильный ответ: {report['correct']}\n")


questions = load_questions('quiz.txt') #файл в формате txt
run_quiz(questions)

