$(function () {
    $('[data-selectize]').each(function (index, el) {
        var selectizeOptions = {};
        // We parse attributes in order to set appropriate options for selectize component
        var attributes = $(el)[0].attributes;
        $.each(attributes, function (index, attr) {
            if (attr.name.startsWith("selectize-")) {
                var selectizeKey = attr.name.replace("selectize-", "");
                selectizeKey = selectizeKey.replace(/-([a-z])/g, function (m, w) {
                    return w.toUpperCase();
                });
                // Cast string value into respective value
                var value = $.isNumeric(attr.value) ? parseInt(attr.value) : attr.value;
                value = (value == "True") ? true : value;
                value = (value == "False") ? false : value;

                var accepted = ["load", "score", "render", "onChange", "onInitialize", "onItemAdd", "onItemRemove",
                    "onClear", "onOptionAdd", "onOptionRemove", "onOptionClear", "onOptionGroupAdd",
                    "onOptionGroupRemove", "onOptionGroupClear", "onDropdownOpen", "onDropdownClose",
                    "onType", "onDelete"];

                if (accepted.includes(selectizeKey)) {
                    value = eval(value);
                    if (value == undefined) {
                        console.warn("Function not defined: " + attr.value);
                    }
                }
                if (selectizeKey == 'plugins') {
                    value = value.split(',');
                }
                selectizeOptions[selectizeKey] = value;
            }
        });
        $(el).selectize(selectizeOptions);
    });
});
