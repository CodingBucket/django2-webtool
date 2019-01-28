var firstFilter = true
var secondFilter = true
var thirdFilter = true

var hasFirstValue = true
var hasSecondValue = false
var hasthirdValue = false

var container = []

if (firstFilter) {
    hasFirstValue = true

    // first, second & third filter

    // first & second filter

    // second & third filter

    // only first filter

    if (secondFilter && hasSecondValue && hasFirstValue) {
        // first & second filter
        return container  
    } else if (hasFirstValue) { 
        // only first filter
        return container
    }
}



var activeFilters = [
    { text: 'On ship', name: 'transport', value: 'ship', isSelected: true },
    //{ text: 'On truck', value: 'truck', isSelected: true },
    //{ text: 'On heli', value: 'helicopter', isSelected: true },
    { text: 'search', name: 'id' , value: '5', isSelected: true },
    { text: 'status', name: 'status', value: 'arriving', isSelected: true },
];

containers = ["c1", "c2", "c3"]

let matchingContainers = containers.filter(container => {
    isMismatched = false
    activeFilters.forEach(af => {
        if (container[af.name] !== af.value) {
            isMismatched = true
        }
    });
    if (!isMismatched) return container;
})