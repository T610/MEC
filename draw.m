

%% 设置导入选项并导入数据
opts = spreadsheetImportOptions("NumVariables", 1);

% 指定工作表和范围
opts.Sheet = "Sheet1";
opts.DataRange = "A2:A2001";

% 指定列名称和类型
opts.VariableNames = "UE";
opts.VariableTypes = "double";

% 导入数据
tbl = readtable("C:\Users\15212\Desktop\MEC1118\MEC1118\wolf.xlsx", opts, "UseExcel", false);

%% 转换为输出类型
wolf = tbl.UE;

%% 设置导入选项并导入数据
opts = spreadsheetImportOptions("NumVariables", 1);

% 指定工作表和范围
opts.Sheet = "Sheet1";
opts.DataRange = "A2:A2001";

% 指定列名称和类型
opts.VariableNames = "UE";
opts.VariableTypes = "double";

% 导入数据
tbl = readtable("C:\Users\15212\Desktop\MEC1118\MEC1118\local.xlsx", opts, "UseExcel", false);

%% 转换为输出类型
local = tbl.UE;


%% 设置导入选项并导入数据
opts = spreadsheetImportOptions("NumVariables", 1);

% 指定工作表和范围
opts.Sheet = "Sheet1";
opts.DataRange = "A2:A2001";

% 指定列名称和类型
opts.VariableNames = "UE";
opts.VariableTypes = "double";

% 导入数据
tbl = readtable("C:\Users\15212\Desktop\MEC1118\MEC1118\mec.xlsx", opts, "UseExcel", false);

%% 转换为输出类型
mec = tbl.UE;




%%
Step = [1:1:2000];

plot(Step,wolf,'r')
hold
plot(Step,local,'m')
hold on
plot(Step,mec,'g')
hold on



xlabel('Episode')
ylabel('Reward')

legend('wolf-phc','local only','mec only')