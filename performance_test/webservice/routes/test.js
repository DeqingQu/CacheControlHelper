var express = require('express');
var router = express.Router();

/* GET test listing. */

router.get('/', function(req, res, next) {
    var test_id = "None"
    res.set({'content-type': 'application/json;charset=utf-8'});
    data = {'id': test_id, "data": {'concept_class_id': 'Clinical Finding', 'concept_code': '92546004', 'concept_count': 368.0, 'concept_id': 192855, 'concept_name': 'Cancer in situ of urinary bladder', 'domain_id': 'Condition', 'vocabulary_id': 'SNOMED'}};
    res.status(200).end(JSON.stringify(data));
});

router.get('/:id', function(req, res, next) {
    var test_id = req.params['id'];
    res.set({'content-type': 'application/json;charset=utf-8'});
    data = {'id': test_id,
            "data0": {'concept_class_id': 'Clinical Finding', 'concept_code': '92546004', 'concept_count': 368.0, 'concept_id': 192855, 'concept_name': 'Cancer in situ of urinary bladder', 'domain_id': 'Condition', 'vocabulary_id': 'SNOMED'},
            "data1": {'concept_class_id': 'Clinical Finding', 'concept_code': '92546004', 'concept_count': 368.0, 'concept_id': 192855, 'concept_name': 'Cancer in situ of urinary bladder', 'domain_id': 'Condition', 'vocabulary_id': 'SNOMED'},
            "data2": {'concept_class_id': 'Clinical Finding', 'concept_code': '92546004', 'concept_count': 368.0, 'concept_id': 192855, 'concept_name': 'Cancer in situ of urinary bladder', 'domain_id': 'Condition', 'vocabulary_id': 'SNOMED'},
            "data3": {'concept_class_id': 'Clinical Finding', 'concept_code': '92546004', 'concept_count': 368.0, 'concept_id': 192855, 'concept_name': 'Cancer in situ of urinary bladder', 'domain_id': 'Condition', 'vocabulary_id': 'SNOMED'},
            "data4": {'concept_class_id': 'Clinical Finding', 'concept_code': '92546004', 'concept_count': 368.0, 'concept_id': 192855, 'concept_name': 'Cancer in situ of urinary bladder', 'domain_id': 'Condition', 'vocabulary_id': 'SNOMED'},
            "data5": {'concept_class_id': 'Clinical Finding', 'concept_code': '92546004', 'concept_count': 368.0, 'concept_id': 192855, 'concept_name': 'Cancer in situ of urinary bladder', 'domain_id': 'Condition', 'vocabulary_id': 'SNOMED'},
            "data6": {'concept_class_id': 'Clinical Finding', 'concept_code': '92546004', 'concept_count': 368.0, 'concept_id': 192855, 'concept_name': 'Cancer in situ of urinary bladder', 'domain_id': 'Condition', 'vocabulary_id': 'SNOMED'},
            "data7": {'concept_class_id': 'Clinical Finding', 'concept_code': '92546004', 'concept_count': 368.0, 'concept_id': 192855, 'concept_name': 'Cancer in situ of urinary bladder', 'domain_id': 'Condition', 'vocabulary_id': 'SNOMED'},
            "data8": {'concept_class_id': 'Clinical Finding', 'concept_code': '92546004', 'concept_count': 368.0, 'concept_id': 192855, 'concept_name': 'Cancer in situ of urinary bladder', 'domain_id': 'Condition', 'vocabulary_id': 'SNOMED'},
            "data9": {'concept_class_id': 'Clinical Finding', 'concept_code': '92546004', 'concept_count': 368.0, 'concept_id': 192855, 'concept_name': 'Cancer in situ of urinary bladder', 'domain_id': 'Condition', 'vocabulary_id': 'SNOMED'}
            };
    res.status(200).end(JSON.stringify(data));
});

module.exports = router;
