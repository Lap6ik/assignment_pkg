import pytest

from methodExercise import arrayflatenner

def test_check_array1():
    a = [[1,2,[3,8]],4,12,[72, 94, [11,12,[1,2,[18,[19,[1]]]]]]]
    print("The result:")
    print(arrayflatenner.flattenArray(a))
    assert arrayflatenner.flattenArray(a) == [1,2,3,8,4,12,72,94,11,12,1,2,18,19,1]

def test_check_array2():
    l = (1,18,(19,6,(100,32)))
    assert arrayflatenner.flattenArray(l) == [1,18,19,6,100,32]

def test_check_string():
    l="mhdkkgfj"
    print(arrayflatenner.flattenArray(l))
    assert arrayflatenner.flattenArray("mhdkkgfj") == ["mhdkkgfj"]

def test_check_dictionary():
    l = {"gh":888, "fh":999}
    with pytest.raises(KeyError):
        arrayflatenner.flattenArray(l)

#testing how to flatten array as string
def test_check2_array1():
    a = [[1,2,[3,8]],4,12,[72, 94, [11,12,[1,2,[18,[19,[1]]]]]]]
    print(arrayflatenner.flattenAsString(a)==[1,2,3,8,4,12,72,94,11,12,1,2,18,19,1])

def test_check2_array2():
    l = (1,18,(19,6,(100,32)))
    #print(arrayflatenner.flattenAsString(l))
    assert arrayflatenner.flattenAsString(l)==[1,18,19,6,100,32,]

    