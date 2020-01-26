$(document).ready(function() {

const form = document.querySelector('form');
// const userInfoTable = form.querySelector('.person-info-table')

const createGroup = () => `
    <div class="group">
    <input type="text" name="item[]" placeholder="item">
    <input type="text" name="price[]" placeholder="price">
    <button class="remove" type="button" name="remove[]">Remove</button>
    </div>
`;

const userGroup = () => 
    `<div class="person-info-table shadow">
        <div class="items">
            <div class="person-name">
                <input type="text" placeholder="Person1">
                <input type="text" placeholder="Amount Paid">
            </div>
            <button type="submit" name="submit" class="submit">Submit</button>
            <div class="group">
                <input type="text" name="item[]" placeholder="item">
                <input type="text" name="price[]" placeholder="price">
                <button class="remove" type="button" name="remove[]">Remove</button>
            </div>
        </div>
        <div class="controls">
            <button class="add" type="button" name="add">Add Group</button>
        </div>
    </div>
`;

var i = 0;
var x = '{{ i }}';
for(i=0;i<x-1;i++) {
    const group = userGroup();
    form.insertAdjacentHTML("beforeend", group);
}


function insertItems(userInfoTable){
    userInfoTable.addEventListener("click", function(event) {
    const addButton = event.target.closest('.add');
    const removeButton = event.target.closest('.remove');
    const items = userInfoTable.querySelector(".items");
    if(addButton !== null) {
        const group = createGroup();
        items.insertAdjacentHTML('beforeend', group);
    }

    removeButton.parentNode.parentNode.removeChild(removeButton.parentNode);
    });
}


var i = 0;
const userInfoTable = document.getElementsByClassName("person-info-table");
// const items = userInfoTable.querySelector('.items');
var len = userInfoTable.length;


for( ; i < len ; i++){
    insertItems(userInfoTable[i]);
}
// userInfoTable.addEventListener('click', function(event) {
//     const addButton = event.target.closest('.add');
//     const removeButton = event.target.closest('.remove');

//     if(addButton !== null) {
//         const group = createGroup();
//         items.insertAdjacentHTML('beforeend', group);
//     }

//    removeButton.parentNode.parentNode.removeChild(removeButton.parentNode);
// });


});