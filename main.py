# this equation and example has been create and made solely from just this gif and seeing how bubble sorting works.
# https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif
# by: isaac lyne

def start():
    # copy below numbers if you havent got any to sort, and you are wanting to test:
    # 2, 10, 2, 6, 8, 100, 62, 32, 1, 60, 3, 6, 3, 4, 5, 8, 2, 9, 10, 290, 12, 52, 3, 162, 15
    items = input('Input number to sort, in this format (2,3,5,1,6,)').split(',')
    format_tems = []
    for item in items:
        format_tems.append(int(item.strip()))
    print(format_tems)
    order = input('Sort number items asc or desc: ').lower().strip()
    if order != 'asc' and order != 'desc':
        print('incorrect input: please enter either "asc", or "desc"')
    else:
        sort(format_tems, order)

def sort(items, order):
    sorted_items = []
    if order == 'asc': # if chosen ascending sort
        index = len(items) - 1 # set index to the length to start from the end (-1 to setup for the first check where we check +1, if we keep it withou -1 it will throw out of range error)

        # while loop to continually sort and go through until the index >= 0 meaning the sorting has been completed
        # the index will be below 0 as soon as it has completed sorting, as it will continue going down trying to find one to sort, 
        # however there is none so it goes below 0
        while index >= 0:  
            for j in range(index): # go through all items in the list 
                if items[j] > items[j+1]: # if the item[j] is greater than the next item in the list then swap spots
                    items[j], items[j+1] = items[j+1], items[j]
            index -= 1 # go down one item to start the next check
        print(items) # print the final list that is sorted
    elif order == 'desc':
        index = len(items) - 1
        while index >= 0:
            for j in range(index):
                if items[j] < items[j+1]: # only thing to change is to make sure it is checking if it is smaller than rather than greater than
                    items[j], items[j+1] = items[j+1], items[j]
            index -= 1
        print(items)
    print('Completed sort')

    
start()
