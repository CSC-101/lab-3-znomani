def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body.
    return total

result = tally([4, 9, 2, 1]) #total(4)=0+4=4, total(9)=4+9=13, total(2)=13+2=15, total(1)=15+1=16

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body.
    return new_list                    # How does this loop differ from that above?
#idx[0]=4, idx[1,]=9, idx[2]=2, idx[3]=1
#result = new_list = [4,9,2,1]
result = copy([4, 9, 2, 1])

def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body.
    return new_list
#[4+1=5, 9+1=10, 2+1=3, 1+1=2] => new_list = [5,10,3,2]
result = increment_all([4, 9, 2, 1])
