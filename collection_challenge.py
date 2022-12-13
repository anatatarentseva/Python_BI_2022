DNA = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'T', 'g': 'c', 'c': 'g', 't': 'a', 'a': 't'}
RNA = {'G': 'C', 'C': 'G', 'U': 'A', 'A': 'U', 'g': 'c', 'c': 'g', 'u': 'a', 'a': 'u'}


def check_sequence(sequence):
    trust = set(sequence) <= set(DNA.keys())
    if trust:
        return True, 'DNA'
    trust = set(sequence) <= set(RNA.keys())
    if trust:
        return True, 'RNA'
    else:
        return False, ''


def transcribe(sequence, type):
    result = []
    for nucleotide in sequence:
        if nucleotide == 'T':
            result.append('U')
        elif nucleotide == 't':
            result.append('u')
        else:
            result.append(nucleotide)
    return "".join(result)


def complement(sequence, type):
    mapping = {'DNA': DNA, 'RNA': RNA}
    result = ''
    for nucleotide in sequence:
        result = result + mapping[type][nucleotide]
    return result


def reverse(sequence, type):
    return sequence[::-1]


def reverse_complement(sequence, type):
    reversed_sequence = reverse(sequence, type)
    reversed_complemented = complement(reversed_sequence, type)
    return reversed_complemented


def do_command(command):
    action = {
        'reverse': reverse,
        'complement': complement,
        'reverse complement': reverse_complement
    }
    is_correct = False
    while not is_correct:
        sequence = input("Please enter sequence you want to "
                         + command + ": \n")
        good, type_of_seq = check_sequence(sequence)
        if not good:
            print('Неправильный алфавит! Попробуйте еще раз:')
        else:
            print(action[command](sequence, type_of_seq))
            is_correct = True


if __name__ == "__main__":
    while True:
        inserted_command = input(
            'Please enter command from the list:'
            ' \nexit — завершение исполнения программы\n'
            + 'transcribe — напечатать '
              'транскрибированную последовательность\n'
            + 'reverse — напечатать '
              'перевёрнутую последовательность\n'
            + 'complement — напечатать '
              'комплементарную последовательность\n'
            + 'reverse complement — напечатать обратную '
              'комплементарную последовательность\n')
        if inserted_command == 'exit':
            print("До свидания, до встречи!")
            break
        if inserted_command == 'transcribe':
            correctness = False
            while not correctness:
                enter_sequence = input(
                    'Please enter sequence you want to transcribe:\n')
                correct, type_sequence = check_sequence(enter_sequence)
                if not correct:
                    print('Неправильный алфавит! Попробуйте еще раз:')
                elif type_sequence != 'DNA':
                    print('Данная последовательность не является ДНК! Попробуйте еще раз:')
                elif (type_sequence == 'DNA') and correct:
                    print(transcribe(enter_sequence, type_sequence))
                    correctness = True
                else:
                    print('У нас проблемы!')
        elif inserted_command == 'reverse':
            do_command('reverse')
        elif inserted_command == 'complement':
            do_command('complement')
        elif inserted_command == 'reverse complement':
            do_command('reverse complement')