import re


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


def add(a, b):
    return a+b

expression = '((5-(4-3*5+6))/2)'

count_mul_div = 0
count_brackets = 0

for i in range(len(expression)):
    if expression[i] == '(':
        count_brackets = count_brackets + 1

print count_brackets

for i in range(count_brackets):
    res_brackets = re.search('[+-]?[(][^()]+[)]', expression)
    exp_brackets = res_brackets.group()
    print "RES: %s" % exp_brackets

    for j in range(len(exp_brackets)):
        if exp_brackets[j] == '*' or exp_brackets[j] == '/':
            count_mul_div = count_mul_div + 1
    print count_mul_div


    for k in range(count_mul_div):
        res = re.search(r'[-+]?\d+[*/][-+]?\d+', exp_brackets)
        print "RES1: %s" % res.group()
        symbols = re.split(r'[*/\s]', res.group())
        digits = re.findall(r'[*/\s]', res.group())
        print symbols
        print digits
        if '*' in digits:
            factor1 = int(symbols[digits.index("*")])
            factor2 = int(symbols[digits.index("*") + 1])
            product = mul(factor1, factor2)
            print product
            exp_product = "%s*%s" % (factor1, factor2)
            exp_brackets= exp_brackets.replace(exp_product, str(product))
  #          print expression
        elif '/' in digits:
            dividend = int(symbols[digits.index("/")])
            divisor = int(symbols[digits.index("/") + 1])
            quotient = div(dividend, divisor)
            print quotient
            exp_quotient = "%s/%s" % (dividend, divisor)
            exp_brackets = exp_brackets.replace(exp_quotient, str(quotient))
            print expression
    print exp_brackets

    count_mul_div=0

    outcome_ins = re.findall(r'[-+]?\d+',exp_brackets )
    print outcome_ins
    result = outcome_ins[0]
    for i in range(len(outcome_ins) - 1):
        print outcome_ins
        result = add(int(result), int(outcome_ins[i + 1]))
        print result
    exp_brackets = exp_brackets.replace(exp_brackets, exp_brackets[0]+str(result))
    exp_brackets = exp_brackets.replace('+-', '-')
    exp_brackets = exp_brackets.replace('--', '+')
    expression = expression.replace(res_brackets.group(), str(exp_brackets))


outcome = re.findall(r'[-+]?\d+', expression)
print outcome
result = outcome[0]
for i in range(len(outcome)-1):
    print outcome
    result = add(int(result), int(outcome[i+1]))
print result