feedback = raw_input('Questions ?')
if '?' in feedback:
    if have_answer():
        give_answer()
    else:
        pretend_the_question_is_ill_posed()
else:
    print 'Thanks for your attention.'
