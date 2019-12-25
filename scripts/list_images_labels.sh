#!/usr/bin/env bash

readonly CURRENT_DIR=$(dirname $(realpath $0))

readonly DATA_PATH=$(realpath ${CURRENT_DIR}/../data)

if [ ! -d $DATA_PATH/augmented_data ]; then
    echo "No data found"
    exit 0
fi

readonly IMAGES_PATH=$(realpath ${DATA_PATH}/augmented_data/frames)
readonly LABELS_PATH=$(realpath ${DATA_PATH}/augmented_data/annotations)

readonly ALL_IMAGE_LIST_FILE=${DATA_PATH}/all_train_list.txt
readonly ALL_LABEL_LIST_FILE=${DATA_PATH}/all_label_list.txt

rm -rf ${ALL_IMAGE_LIST_FILE}
rm -rf ${ALL_LABEL_LIST_FILE}
touch ${ALL_IMAGE_LIST_FILE}
touch ${ALL_LABEL_LIST_FILE}

function list_files {
    for f in $1/*; do
        if [ -f ${f} ]; then
            echo ${f} >> $2
        fi
    done
}

list_files ${IMAGES_PATH} ${ALL_IMAGE_LIST_FILE}
list_files ${LABELS_PATH} ${ALL_LABEL_LIST_FILE}
