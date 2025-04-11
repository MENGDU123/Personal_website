function getFileList(directory) {
    var fileList = [];

    // 获取目录下的所有文件/目录
    var files = File(directory).ls();

    // 遍历文件列表
    for (var i = 0; i < files.length; i++) {
        var file = files[i];

        // 判断文件类型，如果是目录则递归获取子目录的文件列表
        if (file.isFolder()) {
            var subDirectory = directory + '/' + file.name;
            var subFiles = getFileList(subDirectory);
            fileList = fileList.concat(subFiles);
        } else {
            fileList.push(file);
        }
    }

    return fileList;
}
//猫猫不会js，这段是直接复制的。
//js目前没有使用到。