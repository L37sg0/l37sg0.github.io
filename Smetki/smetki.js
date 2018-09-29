document.getElementById("formIncome").addEventListener('submit', function(event){event.preventDefault();});
document.getElementById("formCost").addEventListener('submit', function(event){event.preventDefault();});
document.getElementById("formBills").addEventListener('submit', function(event){event.preventDefault();});
function newIncome(element)
{
    var table = document.getElementById(element);
    var name = document.getElementById('incomeName').value
    var price = document.getElementById('incomePrice').value
    
    var newRow = document.createElement("tr");
    var newName = document.createElement("th");
    var newPrice = document.createElement("td");
    newPrice.className = "income";
    var newCurrency = document.createElement("td");
    
    newName.innerHTML = name+":";
    newPrice.innerHTML = price;
    newCurrency.innerHTML = "лв."
    
    
    newRow.appendChild(newName);
    newRow.appendChild(newPrice);
    newRow.appendChild(newCurrency);
    table.appendChild(newRow);
}

function newCost(element)
{
    var table = document.getElementById(element);
    var name = document.getElementById('costName').value
    var price = document.getElementById('costPrice').value
    
    var newRow = document.createElement("tr");
    var newName = document.createElement("th");
    var newPrice = document.createElement("td");
    newPrice.className = "cost";
    var newCurrency = document.createElement("td");
    
    newName.innerHTML = name+":";
    newPrice.innerHTML = price;
    newCurrency.innerHTML = "лв."
    
    
    newRow.appendChild(newName);
    newRow.appendChild(newPrice);
    newRow.appendChild(newCurrency);
    table.appendChild(newRow);
}

function mathBills()
{
    var incomes = document.getElementsByClassName("income");
    var costs = document.getElementsByClassName("cost");
    var bill = 0;
    var savings = 0;
    var daily = 0;
    var credit = 0;
    
    //Math the incomes
    for(i=0;i<incomes.length;i++)
    {
        bill = bill + Number(incomes[i].innerHTML);
    }
    
    //Math the costs
    for(c=0;c<costs.length;c++)
    {
        bill = bill - Number(costs[c].innerHTML);
    }
    
    //Math savings and daily
    
    if(bill<=0)
    {
        //Check if there is a need of credit
        credit = -bill;
        bill = 0;
    }
    else
    {
        savings = bill/5;
        bill = bill - savings;
        daily = bill/30;
    }
    
    
    //Clear the previous result
    var table = document.getElementById("bills")
    while(table.firstChild)
    {
        table.removeChild(table.firstChild);
    };
    
    //Make new output data
    var rowBill = document.createElement("tr");
    rowBill.innerHTML = "Чиста сума:    "+bill;
    var rowSavings = document.createElement("tr");
    rowSavings.innerHTML = "Спестявания:    "+savings;
    var rowDaily = document.createElement("tr");
    rowDaily.innerHTML = "Дневни:   "+daily;
    var rowCredit = document.createElement("tr");
    rowCredit.innerHTML = "Кредит:  "+credit;
    
    table.appendChild(rowBill);
    table.appendChild(rowSavings);
    table.appendChild(rowDaily);
    table.appendChild(rowCredit);
}
