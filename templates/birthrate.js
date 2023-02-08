

function init(){
    let drop = d3.select("#selDataset"); 
    let p = d3.select("li").text("items")
    drop.append("options").property("value",p).text(p);
    console.log(p);
    
};

init();