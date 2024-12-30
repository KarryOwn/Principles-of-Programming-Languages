from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List

# Base Class for AST Nodes
class AST(ABC):
    @abstractmethod
    def accept(self, v):
        pass

# Program Node
@dataclass
class Program(AST):
    statements: List[AST]

    def accept(self, v):
        return v.visitProgram(self)

# Binary Operation Node
@dataclass
class BinOp(AST):
    op: str
    left: AST
    right: AST

    def __str__(self):
        return f"BinOp(\"{self.op}\", {self.left}, {self.right})"

    def accept(self, v):
        return v.visitBinOp(self)

# Integer Literal Node
@dataclass
class Int(AST):
    value: int

    def __str__(self):
        return f"Int({self.value})"

    def accept(self, v):
        return v.visitInt(self)

# Variable Reference Node
@dataclass
class Var(AST):
    name: str

    def __str__(self):
        return f"Var(\"{self.name}\")"

    def accept(self, v):
        return v.visitVar(self)

# Parentheses Node
@dataclass
class Parens(AST):
    expr: AST

    def __str__(self):
        return f"Parens({self.expr})"

    def accept(self, v):
        return v.visitParens(self)

# **New Node: Function Call**
@dataclass
class FuncCall(AST):
    func_name: str
    args: List[AST]

    def __str__(self):
        return f"FuncCall(\"{self.func_name}\", {self.args})"

    def accept(self, v):
        return v.visitFuncCall(self)

# Select Query Node
@dataclass
class Select(AST):
    columns: List[str]
    table: str
    condition: AST

    def __str__(self):
        return f"Select({self.columns}, {self.table}, {self.condition})"

    def accept(self, v):
        return v.visitSelect(self)

# Update Query Node
@dataclass
class Update(AST):
    table: str
    assignment: AST
    condition: AST

    def __str__(self):
        return f"Update({self.table}, {self.assignment}, {self.condition})"

    def accept(self, v):
        return v.visitUpdate(self)

# Insert Query Node
@dataclass
class Insert(AST):
    table: str
    columns: List[str]
    values: List[AST]

    def accept(self, v):
        return v.visitInsert(self)

@dataclass
class Delete(AST):
    table: str
    condition: AST

    def accept(self, v):
        return v.visitDelete(self)

# Assignment Node
@dataclass
class Assignment(AST):
    column: str
    value: AST

    def __str__(self):
        return f"Assignment({self.column}, {self.value})"

    def accept(self, v):
        return v.visitAssignment(self)

# Condition Node
@dataclass
class Condition(AST):
    column: str
    comparator: str
    value: AST

    def __str__(self):
        return f"Condition({self.column}, {self.comparator}, {self.value})"

    def accept(self, v):
        return v.visitCondition(self)

@dataclass
class Value(AST):
    value: str

    def accept(self, v):
        return v.visitValue(self)