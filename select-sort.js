function findSmallest(arr) {
  let smallestValue = arr[0];
  let smallestIndex = 0;

  for (let j = 1; j < arr.length; j++) {
    if (arr[j] < smallestValue) {
      smallestValue = arr[j];
      smallestIndex = j;
    }
  }

  return {
    smallestValue,
    smallestIndex
  }
}

function sort(arr) {
  const sorted = [];
  const len = arr.length;

  for (let i = 0; i < len; i++) {
    const { smallestValue, smallestIndex } = findSmallest(arr);

    sorted.push(smallestValue);

    // Change the length of the array to exclude the smallest value
    arr.splice(smallestIndex, 1);
  }

  return sorted;
}

const arr = [1, 4, 5, 9, 10, 34, 2];
console.log(sort(arr));
