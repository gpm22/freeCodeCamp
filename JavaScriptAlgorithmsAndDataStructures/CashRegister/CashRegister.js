function checkCashRegister(price, cash, cid) {
  let changeObject = {
    status: "OPEN",
    change: [],
  };

  const cashValue = [100, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01];

  let change = cash - price;

  let cidReversed = cid.slice().reverse();

  let totalCid = 0;

  cid.forEach((i) => {
    totalCid += i[1];
  });

  if (change == totalCid) {
    changeObject.status = "CLOSED";
    changeObject.change = cid.slice();
    return changeObject;
  }

  for (let i = 0; i < cashValue.length; i++) {
    let changeValue = Math.floor(change/cashValue[i]) * cashValue[i];

    if (changeValue > cidReversed[i][1]) {
      changeValue = cidReversed[i][1];
    }

    if (changeValue > 0) {
      changeObject.change.push([cidReversed[i][0], changeValue]);
      change = Number.parseFloat(change-changeValue).toPrecision(6);
    }
  }
   
  console.log("changeObject.change: " + changeObject.change);
  if (change > 0) {
    changeObject.status = "INSUFFICIENT_FUNDS";
    changeObject.change = [];
    return changeObject;
  }

  return changeObject;
}

const testCases = [
  [
    19.5,
    20,
    [
      ["PENNY", 1.01],
      ["NICKEL", 2.05],
      ["DIME", 3.1],
      ["QUARTER", 4.25],
      ["ONE", 90],
      ["FIVE", 55],
      ["TEN", 20],
      ["TWENTY", 60],
      ["ONE HUNDRED", 100],
    ],
    { status: "OPEN", change: [["QUARTER", 0.5]] },
  ],
  [
    3.26,
    100,
    [
      ["PENNY", 1.01],
      ["NICKEL", 2.05],
      ["DIME", 3.1],
      ["QUARTER", 4.25],
      ["ONE", 90],
      ["FIVE", 55],
      ["TEN", 20],
      ["TWENTY", 60],
      ["ONE HUNDRED", 100],
    ],
    {
      status: "OPEN",
      change: [
        ["TWENTY", 60],
        ["TEN", 20],
        ["FIVE", 15],
        ["ONE", 1],
        ["QUARTER", 0.5],
        ["DIME", 0.2],
        ["PENNY", 0.04],
      ],
    },
  ],
  [
    19.5,
    20,
    [
      ["PENNY", 0.01],
      ["NICKEL", 0],
      ["DIME", 0],
      ["QUARTER", 0],
      ["ONE", 0],
      ["FIVE", 0],
      ["TEN", 0],
      ["TWENTY", 0],
      ["ONE HUNDRED", 0],
    ],
    { status: "INSUFFICIENT_FUNDS", change: [] },
  ],
  [
    19.5,
    20,
    [
      ["PENNY", 0.01],
      ["NICKEL", 0],
      ["DIME", 0],
      ["QUARTER", 0],
      ["ONE", 1],
      ["FIVE", 0],
      ["TEN", 0],
      ["TWENTY", 0],
      ["ONE HUNDRED", 0],
    ],
    { status: "INSUFFICIENT_FUNDS", change: [] },
  ],
  [
    19.5,
    20,
    [
      ["PENNY", 0.5],
      ["NICKEL", 0],
      ["DIME", 0],
      ["QUARTER", 0],
      ["ONE", 0],
      ["FIVE", 0],
      ["TEN", 0],
      ["TWENTY", 0],
      ["ONE HUNDRED", 0],
    ],
    {
      status: "CLOSED",
      change: [
        ["PENNY", 0.5],
        ["NICKEL", 0],
        ["DIME", 0],
        ["QUARTER", 0],
        ["ONE", 0],
        ["FIVE", 0],
        ["TEN", 0],
        ["TWENTY", 0],
        ["ONE HUNDRED", 0],
      ],
    },
  ],
];

testCases.forEach((i) => {
  let value = checkCashRegister(i[0], i[1], i[2]);
  console.log(
    i[0] +
      " - " +
      i[1] +
      " - " +
      i[2] +
      " -> " +
      i[3].status +
      " - " +
      i[3].change +
      " - Answer: " +
      value.status +
      " - " +
      value.change +
      " - equals? " +
      (value.status === i[3].status && arraysEqual(value.change, i[3].change)
        ? "Yes"
        : "No")
  );
});

function arraysEqual(a, b) {
  if (a === b) return true;
  if (a == null || b == null) return false;
  if (a.length !== b.length) return false;

  for (var i = 0; i < a.length; ++i) {
    if (a[i].length > 1) {
      return arraysEqual(a[i], b[i]);
    }

    if (a[i] !== b[i]) return false;
  }
  return true;
}

