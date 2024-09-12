from django.shortcuts import render

def calculator_view(request):
    if request.method == 'POST':
        try:
            first_num = float(request.POST.get('first_num'))
            second_num = float(request.POST.get('second_num'))
            operation = request.POST.get('operation')

            if operation == 'add':
                result = first_num + second_num
            elif operation == 'subtract':
                result = first_num - second_num
            elif operation == 'multiply':
                result = first_num * second_num
            elif operation == 'divide':
                result = first_num / second_num if second_num != 0 else 'Error'
            else:
                result = 'Invalid Operation'
        except (ValueError, TypeError):
            result = 'Invalid Input'
        
        context = {
            'result': result,
            'first_num': first_num,
            'second_num': second_num,
            'operation': operation
        }
    else:
        context = {}
    
    return render(request, 'calculator/calculator.html', context)
