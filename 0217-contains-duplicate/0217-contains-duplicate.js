/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let m = new Map();

    for (let i = 0; i < nums.length; i++){
        console.log("i = ",i)
        if (m.has(nums[i])){
            console.log("tem = ", nums[i])
            // m.set[`${nums[i]}`, m.get('key') += 1];
            return true
        }
        else{
            console.log("Não tem= ", nums[i])
            m.set(nums[i], 1); 
        }
    }

    return false
    
};